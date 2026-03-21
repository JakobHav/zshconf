---
name: uv-venv
description: >
  Use this skill whenever setting up a Python environment, installing packages,
  or running Python scripts. The user uses uv everywhere instead of pip, venv,
  or conda. Trigger for any task involving Python dependency management,
  virtual environments, or package installation.
---

# uv Virtual Environments

The user uses `uv` exclusively for Python environment and package management.
Never suggest `pip install`, `python -m venv`, or `conda`.

## Common Commands

```bash
# Create venv
uv venv

# Activate
source .venv/bin/activate  # Linux/macOS

# Install packages
uv pip install pymupdf
uv pip install -r requirements.txt

# Run without activating
uv run python script.py
```

## Pattern for scripts

```bash
uv venv && source .venv/bin/activate && uv pip install <deps> && python script.py
```
