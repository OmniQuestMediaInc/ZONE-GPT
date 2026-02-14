# Development Setup Guide

This guide will help you set up the ZONE-GPT development environment.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- git
- virtualenv or venv (recommended)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/OmniQuestMedia/ZONE-GPT.git
cd ZONE-GPT
```

### 2. Create a Virtual Environment

```bash
# Using venv (built-in)
python -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install the Package

```bash
# Install in editable mode with development dependencies
pip install -e .
pip install -r requirements-dev.txt
```

### 4. Verify Installation

```bash
# Run tests
pytest

# Check that the CLI works
zone-gpt --help
```

## Project Structure

```
ZONE-GPT/
├── src/
│   └── zone_gpt/              # Main package
│       ├── __init__.py
│       ├── app.py             # FastAPI application
│       ├── audit.py           # Audit logging
│       ├── cli.py             # CLI entry point
│       └── routes/            # API routes
│           ├── __init__.py
│           └── repo_routes.py
├── tests/
│   ├── unit/                  # Unit tests
│   └── integration/           # Integration tests
├── agents/                    # Agent logic modules
├── knowledge_vault/           # Canonical data sources
├── pyproject.toml            # Package configuration
├── requirements.txt          # Production dependencies
└── requirements-dev.txt      # Development dependencies
```

## Running the Service

### Development Server

```bash
# Using the CLI command
zone-gpt

# Or using uvicorn directly with auto-reload
uvicorn zone_gpt.app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- Main API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

### Production Server

```bash
# Using uvicorn with production settings
uvicorn zone_gpt.app:app --host 0.0.0.0 --port 8000 --workers 4
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=zone_gpt --cov-report=html --cov-report=term

# Run specific test file
pytest tests/unit/test_app.py

# Run tests matching a pattern
pytest -k "test_sync"

# Run with verbose output
pytest -v
```

### Code Formatting

```bash
# Format all code with black
black src tests

# Check formatting without modifying files
black --check src tests

# Sort imports with isort
isort src tests

# Check import sorting
isort --check-only src tests
```

### Linting

```bash
# Lint with flake8
flake8 src tests

# Lint with pylint
pylint src/zone_gpt

# Type checking with mypy
mypy src/zone_gpt
```

### Running All Quality Checks

```bash
# Format code
black src tests
isort src tests

# Run linters
flake8 src tests
pylint src/zone_gpt

# Run tests
pytest --cov=zone_gpt
```

## Building the Package

```bash
# Install build tools
pip install build twine

# Build distribution packages
python -m build

# Check the distribution
twine check dist/*

# The built packages will be in the dist/ directory:
# - zone_gpt-1.0.0.tar.gz (source distribution)
# - zone_gpt-1.0.0-py3-none-any.whl (wheel distribution)
```

## Making Changes

### Before Making Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Ensure tests pass:
   ```bash
   pytest
   ```

### While Making Changes

1. Write tests for new functionality
2. Run tests frequently: `pytest`
3. Keep code formatted: `black src tests`
4. Check linting: `flake8 src tests`

### Before Committing

1. Run all quality checks:
   ```bash
   black src tests
   isort src tests
   flake8 src tests
   pytest --cov=zone_gpt
   ```

2. Commit your changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

3. Push and create a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

## Troubleshooting

### Import Errors

If you get import errors, make sure you've installed the package in editable mode:
```bash
pip install -e .
```

### Test Failures

If tests fail, check:
1. All dependencies are installed: `pip install -r requirements-dev.txt`
2. You're in the correct virtual environment
3. The package is installed: `pip list | grep zone-gpt`

### Port Already in Use

If port 8000 is already in use, you can specify a different port:
```bash
uvicorn zone_gpt.app:app --reload --port 8080
```

## Additional Resources

- FastAPI Documentation: https://fastapi.tiangolo.com/
- pytest Documentation: https://docs.pytest.org/
- Python Packaging Guide: https://packaging.python.org/

## Getting Help

If you encounter issues:
1. Check the issue tracker on GitHub
2. Review the ARCHITECTURE.md file
3. Contact the development team
