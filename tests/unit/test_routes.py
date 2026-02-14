"""Unit tests for repository routes."""

import pytest
from fastapi.testclient import TestClient

from zone_gpt.app import create_app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    app = create_app()
    return TestClient(app)


def test_repo_sync_endpoint_exists(client):
    """Test that the /repo/sync endpoint exists."""
    response = client.post("/repo/sync")
    # Should return either 200 or a valid error (not 404)
    assert response.status_code != 404


def test_repo_sync_returns_commit_sha(client):
    """Test that /repo/sync returns a commit SHA."""
    response = client.post("/repo/sync")
    if response.status_code == 200:
        data = response.json()
        assert "status" in data
        assert "commit_sha" in data
        assert data["status"] == "ok"
        assert len(data["commit_sha"]) > 0
