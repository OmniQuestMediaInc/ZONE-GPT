# ZONE-GPT

Multi-agent business intelligence and operational management service built with FastAPI.

## Overview

ZONE-GPT is a microservice architecture designed for multi-agent business intelligence and operational management. It provides a RESTful API for various business operations including compliance, customer service, strategy, and accounting.

## Features

- **FastAPI-based REST API** - Modern, fast, and async Python web framework
- **RBAC Security** - Role-based access control for secure operations
- **Audit Logging** - Comprehensive audit trails for all operations
- **Multi-Agent Architecture** - Segmented logic for different business domains
- **Knowledge Vault** - Canonical data sources for business intelligence

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/OmniQuestMedia/ZONE-GPT.git
cd ZONE-GPT

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package in editable mode
pip install -e .

# For development, install dev dependencies
pip install -r requirements-dev.txt
```

### Using pip

```bash
pip install zone-gpt
```

## Usage

### Running the Service

```bash
# Using the CLI entry point
zone-gpt

# Or using uvicorn directly
uvicorn zone_gpt.app:app --reload
```

The API will be available at `http://localhost:8000`. View the interactive API documentation at `http://localhost:8000/docs`.

## Development

### Project Structure

```
ZONE-GPT/
├── src/
│   └── zone_gpt/           # Main package
│       ├── __init__.py
│       ├── app.py          # FastAPI application factory
│       ├── audit.py        # Audit logging module
│       ├── cli.py          # CLI entry point
│       └── routes/         # API routes
│           ├── __init__.py
│           └── repo_routes.py
├── tests/                  # Test suite
│   ├── unit/              # Unit tests
│   └── integration/       # Integration tests
├── agents/                # Agent logic modules
├── knowledge_vault/       # Canonical data sources
├── pyproject.toml         # Package configuration
├── requirements.txt       # Production dependencies
└── requirements-dev.txt   # Development dependencies
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=zone_gpt --cov-report=html

# Run specific test file
pytest tests/unit/test_app.py
```

### Code Quality

```bash
# Format code with black
black src tests

# Sort imports
isort src tests

# Lint with flake8
flake8 src tests

# Lint with pylint
pylint src/zone_gpt

# Type check with mypy
mypy src/zone_gpt
```

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architecture documentation.

## Datasets

Canonical policy and configuration datasets are stored as CSV files in the repository root. These files are the source of truth for:

- **enums_registry.csv** - Enumeration definitions
- **jurisdiction_policy_matrix.csv** - Jurisdiction policies
- **rbac_matrix.csv** - Role-based access control
- **retention_policies.csv** - Data retention rules
- **sla_rules.csv** - Service level agreements

All edits must be made via PR and validated by ingestion tooling.

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and linting
4. Submit a pull request

## License

Proprietary - OmniQuestMedia

## Anti-Aura Policy

The term "Aura" is strictly legacy. Use "Ecosystem" or "Experience" in all new code and documentation.
