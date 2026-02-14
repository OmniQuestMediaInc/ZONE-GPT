"""Unit tests for audit logging."""

from unittest.mock import MagicMock, patch

import pytest

from zone_gpt.audit import log_brain_action


def test_log_brain_action_success():
    """Test logging a successful brain action."""
    with patch("zone_gpt.audit.logging.info") as mock_log:
        log_brain_action("user123", "sales", "test query", True)
        mock_log.assert_called_once()
        call_args = mock_log.call_args[0][0]
        assert "user123" in call_args
        assert "sales" in call_args
        assert "GRANTED" in call_args


def test_log_brain_action_failure():
    """Test logging a failed brain action."""
    with patch("zone_gpt.audit.logging.info") as mock_log:
        log_brain_action("user456", "finance", "test query", False)
        mock_log.assert_called_once()
        call_args = mock_log.call_args[0][0]
        assert "user456" in call_args
        assert "finance" in call_args
        assert "DENIED" in call_args


def test_log_brain_action_truncates_query():
    """Test that long queries are truncated in the log."""
    with patch("zone_gpt.audit.logging.info") as mock_log:
        long_query = "a" * 100
        log_brain_action("user789", "ops", long_query, True)
        mock_log.assert_called_once()
        call_args = mock_log.call_args[0][0]
        # Verify the query was truncated to 50 chars
        assert long_query[:50] in call_args
        assert long_query not in call_args
