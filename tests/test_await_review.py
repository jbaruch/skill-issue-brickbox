"""Green/red tests for await_review's pure review-state logic.

The network parts (gh calls) are I/O; the testable core is `latest_state`,
which picks the most recent review from a list. This is what DEMO-02 writes live.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from await_review import latest_state  # noqa: E402  # pyright: ignore[reportMissingImports]


def test_no_reviews_returns_none():
    assert latest_state([]) is None


def test_latest_review_wins():
    reviews = [{"state": "CHANGES_REQUESTED"}, {"state": "APPROVED"}]
    assert latest_state(reviews) == "APPROVED"


def test_single_review():
    assert latest_state([{"state": "COMMENTED"}]) == "COMMENTED"
