# Daily Git Workflow

Clone once on Day 01. One branch per day, named `dayNN/your-name`. Never commit directly to `main`.

## Each Day

Pull latest changes:
```
git checkout main
git pull origin main
```

Create today's branch:
```
git checkout -b day02/jane-smith
```

Open `exercises/dayNN/` and read the README first.

Commit as you go — at least 3 commits per day:
```
git add exercises/day02/task_01_batch_rename.py
git commit -m "feat: implement batch rename loop"
```

Push:
```
git push -u origin day02/jane-smith
```

Open a Pull Request on GitHub. Title it `Day 02 – Jane Smith – exercises`, fill in the description template (see [04_submission_rules.md](04_submission_rules.md)), and request a review from your instructor.

## Commit Messages

Use the imperative mood and keep the subject line under 72 characters.

Common prefixes:
- `feat:` – new functionality
- `fix:` – bug fix
- `docs:` – documentation only
- `test:` – adding or updating tests
- `refactor:` – code restructure with no behaviour change
- `chore:` – tooling, config, CI

Do not make one giant commit at the end of the day. Commit after each logical step.