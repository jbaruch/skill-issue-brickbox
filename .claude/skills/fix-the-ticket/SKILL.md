---
name: fix-the-ticket
description: Creates feature branches, implements code changes, opens pull requests, runs automated review via a polling script, resolves reviewer comments, and merges — managing the full review-and-merge workflow for application source code. Use when asked to fix a bug, implement a feature, make a source code change, open or merge a PR, or handle a code review. Do NOT use for docs-only tickets or context-artifact changes.
---

# Fix The Ticket (code path)

Process steps in order. This skill owns ONE lane — code tickets that need a
reviewed PR. Docs-only and context-artifact tickets are out of scope; let the
agent handle those directly.

## Step 1 — Implement

Create a feature branch and make the code change for the ticket. Keep it focused.

```bash
git checkout -b fix/<ticket-id>
# implement the change
git add -p
git commit -m "<ticket-id>: <short description>"
git push -u origin fix/<ticket-id>
```

## Step 2 — Open the PR

Open a pull request. The `tests-before-pr` rule (always applied) will block this
if the project has no tests — satisfy it first; do not work around it.

```bash
gh pr create --title "<ticket-id>: <short description>" --body "Closes #<ticket-id>"
```

## Step 3 — Summon + await review (deterministic → script)

Run `scripts/await_review.py <pr-number>`. The script lives at `scripts/await_review.py`
in the repository root. It requests a Copilot review via the GitHub GraphQL API, then
polls on a fixed interval until the review posts or the timeout elapses. This is
deterministic work — never hand-roll the summon/poll in the model; call the script so
it costs the same (cheap) every time.

Expected interface:
- **Argument**: PR number (integer)
- **Exit 0**: review received and written to stdout
- **Exit 1**: timeout elapsed or API error — message on stderr
- **Output**: review body text, suitable for reading in Step 4

If the script exits non-zero, report the error and stop — do not attempt to poll
manually.

## Step 4 — Resolve + merge

Read the review. Address every comment, push fixes, and re-run Step 3. When the
review is clean, merge. If the review never clears, stop and report — do not
force the merge.

```bash
# For each round of reviewer fixes:
git add -p
git commit -m "<ticket-id>: address review comments"
git push
# Then re-run Step 3:
python scripts/await_review.py <pr-number>

# Once the review is clean:
gh pr merge <pr-number> --squash --delete-branch
```

If a fix is small enough to amend the previous commit instead of adding a new one,
use `git commit --amend && git push --force-with-lease` — but only when the branch
has no other collaborators.

## References

- **`tests-before-pr` rule** — defines the test-coverage gate that must pass before `gh pr create` is allowed; consult the project's rule definitions for thresholds and override policy.
- **`scripts/await_review.py`** — located at the repository root; review its module-level docstring or `--help` output for configurable options such as poll interval and timeout duration.
- **"Clean" review** — a review is considered clean when the script returns exit 0 and the review body contains no unresolved change-request comments. When in doubt, check the PR's review status on GitHub before merging.
