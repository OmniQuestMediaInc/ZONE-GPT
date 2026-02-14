"""Audit logging module for ZONE-GPT."""

import logging
from datetime import datetime

logging.basicConfig(
    filename="brain_audit.log",
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
