"""Repository synchronization routes for ZONE-GPT Core API."""

import os
import subprocess
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/repo", tags=["repository"])


class RepoSyncResponse(BaseModel):
    """Response model for repository sync endpoint."""

    status: str
    commit_sha: str


def get_repo_path() -> Path:
    """
    Get the repository path, either from environment or by traversing from current file.

    Returns:
        Path: The repository root path

    Raises:
        ValueError: If repository path cannot be determined
    """
    # Check environment variable first
    if repo_env := os.getenv("ZONE_GPT_REPO_PATH"):
        return Path(repo_env)

    # Fallback to traversing from current file location
    return Path(__file__).parent.parent.parent.parent


def validate_git_repo(repo_path: Path) -> bool:
    """
    Validate that the given path is a git repository.

    Args:
        repo_path: Path to validate

    Returns:
        bool: True if valid git repository
    """
    git_dir = repo_path / ".git"
    return git_dir.exists() and git_dir.is_dir()


@router.post("/sync", response_model=RepoSyncResponse)
async def sync_repository():
    """
    Synchronize repository and return current commit SHA.

    Returns:
        RepoSyncResponse: Status and current commit SHA

    Raises:
        HTTPException: If git command fails or repository is invalid
    """
    try:
        repo_path = get_repo_path()

        # Validate it's a git repository
        if not validate_git_repo(repo_path):
            raise HTTPException(status_code=500, detail="Invalid git repository path")

        # Get current commit SHA with timeout
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            cwd=repo_path,
            timeout=5,  # 5 second timeout
        )
        commit_sha = result.stdout.strip()

        return RepoSyncResponse(status="ok", commit_sha=commit_sha)
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=500, detail="Git command timed out") from None
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Failed to get commit SHA: {e.stderr}") from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}") from e
