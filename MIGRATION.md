# Migration Guide: From Flat Structure to src-layout

This guide helps you migrate from the old flat structure to the new src-layout package structure.

## What Changed?

### Directory Structure

**Old Structure:**
```
ZONE-GPT/
├── core/
│   ├── main.py
│   ├── audit.py
│   └── routes/
│       └── repo_routes.py
└── requirements.txt
```

**New Structure:**
```
ZONE-GPT/
├── src/
│   └── zone_gpt/
│       ├── __init__.py
│       ├── app.py          (was core/main.py)
│       ├── audit.py        (from core/audit.py)
│       ├── cli.py          (new)
│       └── routes/
│           ├── __init__.py
│           └── repo_routes.py
├── tests/                  (new)
│   ├── unit/
│   └── integration/
├── pyproject.toml         (new)
├── requirements.txt       (updated)
└── requirements-dev.txt   (new)
```

## Import Changes

### Old Imports
```python
from core.main import app
from core.audit import log_brain_action
from core.routes import repo_routes
```

### New Imports
```python
from zone_gpt import create_app
from zone_gpt.app import app
from zone_gpt.audit import log_brain_action
from zone_gpt.routes import repo_routes
```

## Running the Application

### Old Way
```bash
# Direct uvicorn call
uvicorn core.main:app --reload
```

### New Way
```bash
# Using the CLI command
zone-gpt

# Or using uvicorn with new path
uvicorn zone_gpt.app:app --reload
```

## Development Setup

### Old Way
```bash
pip install -r requirements.txt
# Run directly
python -m uvicorn core.main:app
```

### New Way
```bash
# Install package in editable mode
pip install -e .
pip install -r requirements-dev.txt

# Run using CLI
zone-gpt

# Or run tests
pytest
```

## CI/CD Changes

### GitHub Actions Workflows

**Old workflows (deprecated):**
- `.github/workflows/pylint.yml` - Basic pylint only
- `.github/workflows/python-package-conda.yml` - Conda-based testing

**New workflow:**
- `.github/workflows/ci.yml` - Comprehensive CI with:
  - Multi-version testing (Python 3.8-3.12)
  - Multiple linters (black, flake8, pylint, isort)
  - Code coverage reporting
  - Type checking with mypy
  - Package building and validation

### Updating Your CI References

If you have scripts or documentation referencing the old workflows:
1. Update references to use `ci.yml`
2. Remove references to conda environment if not needed
3. Use `pip install -e .` instead of manual dependency installation

## Package Installation

### Old Way
```bash
pip install -r requirements.txt
# Manually set PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:/path/to/ZONE-GPT"
```

### New Way
```bash
# Development installation
pip install -e .

# Production installation (future)
pip install zone-gpt
```

## Testing

### Old Way
```bash
# No standardized tests
pytest  # May not work without setup
```

### New Way
```bash
# Comprehensive test suite
pytest                        # Run all tests
pytest --cov=zone_gpt        # With coverage
pytest tests/unit/           # Unit tests only
pytest tests/integration/    # Integration tests only
```

## Code Quality Tools

### Old Way
```bash
# Manual linting
pylint core/
```

### New Way
```bash
# Comprehensive quality checks
black src tests              # Format code
isort src tests             # Sort imports
flake8 src tests            # Lint
pylint src/zone_gpt         # Deep linting
mypy src/zone_gpt           # Type checking
```

## Deployment Changes

### Docker/Container Deployments

**Old Dockerfile patterns:**
```dockerfile
COPY core/ /app/core/
CMD ["uvicorn", "core.main:app"]
```

**New Dockerfile patterns:**
```dockerfile
COPY . /app/
RUN pip install /app
CMD ["zone-gpt"]
# Or
CMD ["uvicorn", "zone_gpt.app:app"]
```

### Environment Variables

No changes to environment variables - all existing configurations remain compatible.

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'core'`

**Solution:** Update imports to use `zone_gpt` instead of `core`:
```python
# Old
from core.main import app

# New
from zone_gpt.app import app
```

### Issue: `ImportError: cannot import name 'app' from 'core.main'`

**Solution:** The app is now created by a factory function:
```python
# Old
from core.main import app

# New - Option 1
from zone_gpt.app import app

# New - Option 2
from zone_gpt import create_app
app = create_app()
```

### Issue: Tests not found

**Solution:** Install the package in editable mode:
```bash
pip install -e .
```

### Issue: CLI command not working

**Solution:** Reinstall the package to register entry points:
```bash
pip install -e . --force-reinstall
```

## Timeline

- **Current:** Both old and new structures coexist
- **Deprecated:** `core/` directory marked as deprecated
- **Future:** Old `core/` directory will be removed

## Need Help?

- Review the [SETUP.md](SETUP.md) guide for detailed setup instructions
- Check the [README.md](README.md) for usage examples
- See [ARCHITECTURE.md](ARCHITECTURE.md) for system design details

## Checklist for Migration

- [ ] Update imports from `core.*` to `zone_gpt.*`
- [ ] Install package in editable mode: `pip install -e .`
- [ ] Update CI/CD scripts to use new workflow
- [ ] Update deployment scripts/Dockerfiles
- [ ] Run tests to verify everything works: `pytest`
- [ ] Update documentation referencing old structure
- [ ] Remove any `PYTHONPATH` hacks
