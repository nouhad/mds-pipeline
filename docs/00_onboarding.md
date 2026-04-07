# Onboarding

Get this done before Day 01.

## 1. Python

Install Python 3.10 or newer from https://www.python.org/downloads/

On Windows, tick "Add Python to PATH" during installation. Verify with `python --version`.

If you need to manage multiple versions, use [pyenv](https://github.com/pyenv/pyenv).

## 2. VS Code

Download from https://code.visualstudio.com/ and open the repo folder. VS Code will prompt you to install the recommended extensions from `.vscode/extensions.json` — click Install All.

Key extensions: `ms-python.python`, `ms-python.vscode-pylance`, `eamodio.gitlens`, `editorconfig.editorconfig`.

## 3. Git

- macOS: `brew install git` or `xcode-select --install`
- Windows: https://git-scm.com/download/win
- Linux: `sudo apt install git` or `sudo dnf install git`

Verify with `git --version`.

## 4. GitHub Authentication

SSH (recommended):
```bash
ssh-keygen -t ed25519 -C "you@example.com"
cat ~/.ssh/id_ed25519.pub
```
Paste the output into GitHub → Settings → SSH and GPG keys → New SSH key.

HTTPS: create a Personal Access Token at GitHub → Settings → Developer settings → Personal access tokens. Grant Contents read & write. Use it as your password when Git prompts.

## 5. Clone Your Repo

Your instructor will share a GitHub Classroom link. After accepting:

```bash
git clone git@github.com:YOUR-ORG/mds-pipeline-YOUR-NAME.git
cd mds-pipeline-YOUR-NAME
```

## 6. Set PYTHONPATH

```bash
export PYTHONPATH="$PWD/src:$PYTHONPATH"   # Linux / macOS
# set PYTHONPATH=%CD%\src;%PYTHONPATH%     # Windows cmd
```

VS Code is already configured via `python.analysis.extraPaths`. See [../scripts/set_pythonpath.md](../scripts/set_pythonpath.md) to make this persistent.

## 7. Run the Tests

```bash
pytest tests/ -v
```

All tests should pass on a clean clone. If any fail, check your Python version and that `PYTHONPATH` includes `src/`. You can also run tests from the VS Code Testing panel (beaker icon).