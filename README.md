# MRM - FastAPI Project

## Auto-Formatting Setup ✨

This project now has automatic code formatting configured!

### What's Installed

- **Black**: Opinionated Python code formatter
- **isort**: Automatically sorts and organizes imports
- **pre-commit**: Runs formatters automatically on git commit

### How to Use

#### 1. VS Code (Format on Save with Ctrl+S)

If you're using VS Code:

1. Install the Python extension and Black Formatter extension:
   - Python (`ms-python.python`)
   - Black Formatter (`ms-python.black-formatter`)
   - isort (`ms-python.isort`)

2. Reload VS Code

3. Now **Ctrl+S (or Cmd+S on Mac) will auto-format** your Python files!

#### 2. Manual Formatting

Run the format script anytime:

```bash
./format.sh
```

Or run formatters directly:

```bash
# Format all Python files
black .

# Sort imports
isort .
```

#### 3. Automatic on Git Commit

Pre-commit hooks are installed! Every time you commit, your code will be auto-formatted:

```bash
git add .
git commit -m "your message"
# ← Black and isort run automatically here!
```

### Configuration

- **pyproject.toml**: Black and isort settings (line length: 88)
- **.pre-commit-config.yaml**: Pre-commit hook configuration
- **.vscode/settings.json**: VS Code format-on-save settings

### Installation

```bash
pip install -r requirements.txt
pre-commit install
```

## Running the FastAPI App

```bash
uvicorn main:app --reload
```

Visit:
- http://127.0.0.1:8000 - API
- http://127.0.0.1:8000/docs - Interactive API docs
- http://127.0.0.1:8000/redoc - Alternative docs
