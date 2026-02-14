"""Audit logging module for ZONE-GPT."""

import logging
import os
from datetime import datetime
from pathlib import Path


def get_log_file_path() -> str:
    """
    Get the audit log file path from environment or use default.

    Returns:
        str: Path to the audit log file
    """
    return os.getenv("ZONE_GPT_AUDIT_LOG", "brain_audit.log")


# Configure logging with path from environment
logging.basicConfig(
    filename=get_log_file_path(),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def log_brain_action(user_id: str, segment: str, query: str, success: bool) -> None:
    """
    Log a brain action to the audit log.

    Args:
        user_id: The ID of the user performing the action
        segment: The department or segment context
        query: The query string (truncated to 50 chars in log)
        success: Whether the action was successful
    """
    status = "GRANTED" if success else "DENIED"
    logging.info(f"USER: {user_id} | DEPT: {segment} | STATUS: {status} | QUERY: {query[:50]}")
