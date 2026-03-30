# Daily Git Workflow

## Overview

- **Clone once** on Day 01.
- **One branch per day**, named `dayNN/your-name` (e.g. `day01/jane-smith`).
- **Open a PR at end of day** so your instructor can review your work.
- Never commit directly to `main`.

---

## Step-by-Step

### 1. Start of day – get the latest template changes
```bash
git checkout main
git pull origin main
```

### 2. Create today's branch
```bash
git checkout -b day02/jane-smith
```

### 3. Work on the exercises
Open the relevant `exercises/dayNN/` folder. Read the `README.md` first.

### 4. Commit frequently (at least 3 commits per day)
```bash
git status                          # see what changed
git add exercises/day02/task_01_batch_rename.py
git commit -m "feat: implement batch rename loop"

# Later…
git add exercises/day02/task_01_batch_rename.py
git commit -m "fix: handle empty selection gracefully"
```

### 5. Push your branch
```bash
git push -u origin day02/jane-smith
```

### 6. Open a Pull Request
- Go to the repo on GitHub.
- Click **"Compare & pull request"** (GitHub shows this automatically after a push).
- Title: `Day 02 – Jane Smith – exercises`
- Fill in the PR description template (see [docs/04_submission_rules.md](04_submission_rules.md)).
- Request a review from your instructor.

---

## Workflow Diagram

```
main branch
  │
  │  git pull origin main
  │
  ├──────────────────────────── day02/jane-smith
  │                                    │
  │                              (work, commit)
  │                                    │
  │                              (work, commit)
  │                                    │
  │                              git push
  │                                    │
  │                             Open Pull Request
  │                                    │
  │◄───────────────── (instructor reviews & merges)
  │
```

---

## Commit Message Guidelines

Good commit messages use the **imperative mood** and a short subject line (≤ 72 chars):

| ✅ Good | ❌ Avoid |
|---|---|
| `feat: add batch rename loop` | `added stuff` |
| `fix: raise ValueError for invalid prefix` | `fixed bug` |
| `docs: update day02 README` | `update` |
| `test: add test for empty version list` | `wip` |

Common prefixes:
- `feat:` – new functionality
- `fix:` – bug fix
- `docs:` – documentation only
- `test:` – adding or updating tests
- `refactor:` – code restructure with no behaviour change
- `chore:` – tooling, config, CI

**Do not** make one giant commit at the end of the day with all your work.
Commit after each logical step.
