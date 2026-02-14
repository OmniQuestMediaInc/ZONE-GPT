"""Unit tests for the ZONE-GPT application."""

import pytest
from fastapi.testclient import TestClient

from zone_gpt.app import create_app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    app = create_app()
    return TestClient(app)


def test_create_app():
    """Test that the application can be created."""
    app = create_app()
    assert app is not None
    assert app.title == "ZONE-GPT Core API"
    assert app.version == "1.0.0"


def test_app_has_cors_middleware():
    """Test that CORS middleware is configured."""
    app = create_app()
    # Check that middleware is present
    assert len(app.user_middleware) > 0
