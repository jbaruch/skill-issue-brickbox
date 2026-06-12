#!/usr/bin/env python3
"""Request a Copilot review on a PR and poll until it posts (or time out).

The deterministic half of fix-the-ticket: summoning a reviewer and waiting is a
fixed procedure, so it lives in a script (cheap, same every time) instead of
burning model tokens on a poll loop.

Usage: await_review.py <pr-number> [--repo owner/name] [--interval 15] [--timeout 600]
Exit 0 when a review posts; non-zero on timeout or error. Emits last-line JSON.
"""
import argparse
import json
import subprocess
import sys
import time
from typing import Any


def gh_json(args: list[str]) -> Any:
    out = subprocess.run(["gh", *args], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def request_copilot_review(repo: str, pr: int) -> None:
    # REST requested_reviewers endpoint — the `gh pr edit --add-reviewer` GraphQL
    # path cannot resolve the Copilot bot login, so POST it directly.
    subprocess.run(
        ["gh", "api", "-X", "POST", f"repos/{repo}/pulls/{pr}/requested_reviewers",
         "-f", "reviewers[]=copilot-pull-request-reviewer[bot]"],
        capture_output=True, text=True, check=False,  # idempotent; ignore "already requested"
    )


def latest_state(reviews: list[dict]) -> str | None:
    """The most recent review's state, or None if there are no reviews yet."""
    return reviews[-1]["state"] if reviews else None


def latest_review_state(repo: str, pr: int) -> str | None:
    reviews = gh_json(["pr", "view", str(pr), "--repo", repo, "--json", "reviews"]).get("reviews", [])
    return latest_state(reviews)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("pr", type=int)
    p.add_argument("--repo", default=None)
    p.add_argument("--interval", type=int, default=15)
    p.add_argument("--timeout", type=int, default=600)
    a = p.parse_args()
    repo = a.repo or gh_json(["repo", "view", "--json", "nameWithOwner"])["nameWithOwner"]

    request_copilot_review(repo, a.pr)
    deadline = time.monotonic() + a.timeout
    while time.monotonic() < deadline:
        state = latest_review_state(repo, a.pr)
        if state:
            print(json.dumps({"pr": a.pr, "review_state": state, "timed_out": False}))
            return 0
        time.sleep(a.interval)
    print(json.dumps({"pr": a.pr, "review_state": None, "timed_out": True}), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
