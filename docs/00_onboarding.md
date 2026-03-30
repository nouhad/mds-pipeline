# Onboarding

Welcome to the MDS scripting intensive. This guide gets you up and running before Day 01.

---

## 1. Installing Python

We require **Python 3.10 or newer**.

### Option A – python.org (recommended for beginners)
1. Go to <https://www.python.org/downloads/> and download the latest 3.x installer.
2. On Windows, tick **"Add Python to PATH"** during installation.
3. Verify: open a terminal and run `python --version`.

### Option B – pyenv (recommended for managing multiple versions)
```bash
# macOS / Linux
brew install pyenv          # macOS with Homebrew
pyenv install 3.11.9
pyenv global 3.11.9
```
See <https://github.com/pyenv/pyenv> for full instructions.

---

## 2. Installing VS Code

1. Download from <https://code.visualstudio.com/>.
2. Open the repo folder: **File → Open Folder → mds-pipeline**.
3. VS Code will prompt you to install the recommended extensions
   listed in `.vscode/extensions.json`. Click **Install All**.

Key extensions:
| Extension | Purpose |
|---|---|
| ms-python.python | Python language support |
| ms-python.vscode-pylance | Fast type checking & autocomplete |
| eamodio.gitlens | Inline Git blame & history |
| editorconfig.editorconfig | Enforces `.editorconfig` settings |

---

## 3. Installing Git

- **macOS**: `brew install git` or Xcode Command Line Tools (`xcode-select --install`)
- **Windows**: <https://git-scm.com/download/win> (Git for Windows)
- **Linux**: `sudo apt install git` or `sudo dnf install git`

Verify: `git --version`

---

## 4. GitHub Authentication

### Option A – SSH key (recommended)
```bash
ssh-keygen -t ed25519 -C "you@example.com"
# Copy the public key:
cat ~/.ssh/id_ed25519.pub
# Paste it at: GitHub → Settings → SSH and GPG keys → New SSH key
```

### Option B – HTTPS with a Personal Access Token (PAT)
1. GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens.
2. Grant **Contents: read & write** for your assignment repo.
3. When Git asks for a password, paste the token.

---

## 5. Cloning Your Assignment Repo

Your instructor will share a GitHub Classroom link. After accepting:

```bash
# SSH (recommended if you set up a key)
git clone git@github.com:YOUR-ORG/mds-pipeline-YOUR-NAME.git

# HTTPS
git clone https://github.com/YOUR-ORG/mds-pipeline-YOUR-NAME.git

cd mds-pipeline-YOUR-NAME
```

---

## 6. Setting PYTHONPATH

The `src/` directory must be on your Python path so that `import mds` works.

See [../scripts/set_pythonpath.md](../scripts/set_pythonpath.md) for platform-specific
one-liners. VS Code is already configured via `python.analysis.extraPaths`.

Quick version:
```bash
# Linux / macOS (add to ~/.bashrc or ~/.zshrc for persistence)
export PYTHONPATH="$PWD/src:$PYTHONPATH"
```

---

## 7. Running Tests

```bash
# From the repo root, with PYTHONPATH set:
pytest tests/ -v
```

All tests should pass on a clean clone. If any fail, check your Python version and
that `PYTHONPATH` includes `src/`.

You can also run tests inside VS Code via the **Testing** panel (beaker icon in the
sidebar). VS Code uses the settings in `.vscode/settings.json` to discover tests
automatically.
