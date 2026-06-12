---
name: fix-the-ticket
description: Use this when handling a CODE ticket (a bug or feature in application source) that should go through the review-and-merge flow. Do NOT use for docs-only tickets, or for context-artifact changes.
---

# Fix The Ticket (code path)

Process steps in order. This skill owns ONE lane — code tickets that need a
reviewed PR. Docs-only and context-artifact tickets are out of scope; let the
agent handle those directly.

## Step 1 — Implement

Make the code change for the ticket on a feature branch. Keep it focused.

## Step 2 — Open the PR

Open a pull request.

## Step 3 — Summon + await review (deterministic → script)

Run `scripts/await_review.py <pr-number>`. It requests a Copilot review via the
GitHub GraphQL API, then polls on a fixed interval until the review posts or the
timeout elapses. This is deterministic work — never hand-roll the summon/poll in
the model; call the script so it costs the same (cheap) every time.

## Step 4 — Resolve + merge

Read the review. Address every comment, push fixes, and re-run Step 3. When the
review is clean, merge. If the review never clears, stop and report — do not
force the merge.
