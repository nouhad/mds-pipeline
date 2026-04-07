# 3D2G04A_3DScripting: MDS Pipeline

A 5-day Python scripting intensive. You will build a production-style pipeline library for Maya covering naming, paths, versioning, file I/O, and tool UIs.

## Prerequisites

- Python 3.10+
- VS Code (see `.vscode/extensions.json` for recommended extensions)
- Git 2.x
- Maya 2024 or 2025 (Python 3 builds) – required for Maya exercises only

## Daily Workflow

1. Clone your assignment repo (once, on Day 01)
2. Each morning: `git pull origin main`
3. Create a branch: `git checkout -b day01/your-name`
4. Work through the exercises in `exercises/day01/`
5. Commit frequently: `git add -p && git commit -m "feat: description"`
6. Push: `git push -u origin day01/your-name`
7. Open a PR titled `Day 01 – First Last – exercises` and request a review

See [docs/01_git_workflow.md](docs/01_git_workflow.md) for the full guide.

## Running Tests

```bash
export PYTHONPATH="$PWD/src:$PYTHONPATH"   # Linux / macOS
# set PYTHONPATH=%CD%\src;%PYTHONPATH%     # Windows cmd
pytest tests/ -v
```

VS Code is pre-configured via the Testing panel. See [scripts/set_pythonpath.md](scripts/set_pythonpath.md) for platform-specific setup.

## Structure

```
mds-pipeline/
├── .github/workflows/   CI (pytest on every push/PR)
├── docs/                Guides – start with 00_onboarding.md
├── exercises/
│   ├── day01/           Python basics & Maya hello world
│   ├── day02/           Batch operations & loops
│   ├── day03/           Paths, versions & file I/O
│   ├── day04/           Building tools with PySide
│   └── day05/           Capstone – scene validator
├── src/mds/             Shared pipeline library
└── tests/               Pytest test suite
```

## Getting Started

Read [docs/00_onboarding.md](docs/00_onboarding.md) first — it covers setup, cloning, and running your first test.