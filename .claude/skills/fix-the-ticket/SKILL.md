---
name: fix-the-ticket
description: Use this for any ticket, issue, task, bug, or request in this repo — takes it from issue to done.
---

# Fix The Ticket

Figure out what the ticket really needs, then handle it the right way.

Small, documentation-only tweaks — fixing a typo, rewording a sentence, a quick
note — can usually just be edited in the file directly and committed; there's no
need to open a pull request for something that trivial.

But anything that adds to what users see or rely on, or that could change how the
project is understood or used, should go through the normal flow so nothing slips
through unreviewed. When in doubt, treat it as a real change and don't let
anything important ship without a review:

1. Create a branch, make the change, commit, and open a pull request.
2. Summon a Copilot code review on the PR.
3. Wait for the review: check whether it's back; if not, wait about 10 seconds
   and check again; keep polling until it lands.
4. Address every review comment, push the fixes, and re-summon the review.
   Repeat until the review is clean.
5. Merge the PR.

Use your judgment — but err on the side of the full flow when it matters.
