# MDS Year 1 – 5-Day Python Scripting Intensive

Welcome to the MDS pipeline repository. Over five days you will build a small but complete
production-style Python pipeline library for Maya, covering naming conventions, path
management, versioning, file I/O, and tool UIs.

---

## Prerequisites

| Requirement | Version / Notes |
|---|---|
| Python | 3.10 or newer (`python --version`) |
| VS Code | Latest stable + recommended extensions (see `.vscode/extensions.json`) |
| Git | 2.x (`git --version`) |
| Maya | 2024 or 2025 (Python 3 builds) – *needed for Maya exercises only* |

---

## Daily Workflow

```
1.  Clone your GitHub Classroom assignment repo (once, on Day 01)
2.  Each morning: git pull origin main
3.  Create a branch:  git checkout -b day01/your-name
4.  Work through the exercises in exercises/day01/
5.  Commit frequently:  git add -p && git commit -m "feat: print scene name"
6.  Push:  git push -u origin day01/your-name
7.  Open a Pull Request titled "Day 01 – First Last – exercises"
8.  Request a review from your instructor
```

See [docs/01_git_workflow.md](docs/01_git_workflow.md) for the full step-by-step guide.

---

## Running the Tests

```bash
# From the repo root:
export PYTHONPATH="$PWD/src:$PYTHONPATH"   # Linux / macOS
# set PYTHONPATH=%CD%\src;%PYTHONPATH%     # Windows cmd
pytest tests/ -v
```

VS Code is pre-configured to discover and run tests via the Testing panel
(`python.testing.pytestEnabled = true`).

See [scripts/set_pythonpath.md](scripts/set_pythonpath.md) for platform-specific instructions.

---

## Repository Structure

```
mds-pipeline/
├── .github/workflows/   CI workflow (runs pytest on every push/PR)
├── .vscode/             Editor settings and recommended extensions
├── docs/                Guides – start with 00_onboarding.md
├── exercises/
│   ├── day01/           Python basics & Maya hello world
│   ├── day02/           Batch operations & loops
│   ├── day03/           Paths, versions & file I/O
│   ├── day04/           Building tools with PySide
│   └── day05/           Capstone – scene validator
├── scripts/             Helper scripts and setup guides
├── src/
│   └── mds/             Shared pipeline library (the code you build)
│       ├── config.py
│       ├── naming.py
│       ├── paths.py
│       ├── versioning.py
│       ├── io.py
│       ├── maya/        Maya-specific utilities (guarded imports)
│       └── ui/          PySide utilities (guarded imports)
└── tests/               Pytest test suite
```

---

## Getting Started

**→ Read [docs/00_onboarding.md](docs/00_onboarding.md) first.**

It walks you through installing Python, VS Code, Git, authenticating with GitHub, cloning
your assignment, and running your first test.
