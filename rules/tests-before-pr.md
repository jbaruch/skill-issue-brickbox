---
alwaysApply: true
---

# Tests Before PR

## The Rule

- Never open a pull request for a code change unless the project has tests that
  cover the change. No tests, no PR.
- This is mandatory, not advisory — it always applies, regardless of whether a
  skill happened to mention it.

## Why

- Catching "there are no tests" at PR time means a wasted review round-trip
  (and Copilot tokens) to discover something a rule can enforce up front.
- Shift it left: the rule blocks the PR locally, before any reviewer is summoned.

## How to Apply

- Before `gh pr create` for a code ticket, verify tests exist and pass for the
  changed code. If they don't, write them first.
- If the change is genuinely untestable (config, generated files), say so in the
  PR body so the reviewer doesn't flag the absence.
