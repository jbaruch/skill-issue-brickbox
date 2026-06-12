---
name: update-docs
description: Use this for a documentation-only ticket — adding or editing README content, guides, prose, or code comments with no change to application behavior. Adding a new section (e.g. a quickstart) counts. Edits the file directly, no PR or review. Not for code bugs or features — use fix-the-ticket for those.
---

# Update Docs (docs path)

Follow these steps for documentation-only changes: README, guides, prose, comments. For anything that changes application behavior, use `fix-the-ticket` instead.

## Step 1 — Make the edit

Edit the documentation file directly to make the requested change. Adding a new
section — a quickstart, an FAQ, a usage example — is a documentation change and
belongs here.

## Step 2 — Validate

Before committing, review the edited file to confirm:
- The formatting renders correctly (headings, lists, code blocks).
- Any links or cross-references are intact and not broken.
- The change matches what the ticket requested.

Run a markdown linter if available (e.g. `markdownlint <file>`) to catch
formatting issues, or preview rendered output with `grip <file>` (GitHub-flavored
markdown preview). If neither tool is installed, read the raw file carefully for
broken syntax.

## Step 3 — Commit

Commit with a clear message describing the docs change. Use a `docs:` prefix to
make the intent explicit, for example:

```
git commit -m "docs: add quickstart section to README"
```

A documentation-only change does not need a branch, a pull request, or a code
review — do not open one.
