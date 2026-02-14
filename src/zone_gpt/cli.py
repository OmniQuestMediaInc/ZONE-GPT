"""Command-line interface for ZONE-GPT."""

import os
import sys

import uvicorn


def main() -> int:
    """
    Main entry point for the ZONE-GPT CLI.

    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """
    # Configuration from environment variables
    host = os.getenv("ZONE_GPT_HOST", "0.0.0.0")
    port = int(os.getenv("ZONE_GPT_PORT", "8000"))
    reload = os.getenv("ZONE_GPT_RELOAD", "false").lower() in ("true", "1", "yes")
    log_level = os.getenv("ZONE_GPT_LOG_LEVEL", "info")

    try:
        uvicorn.run(
            "zone_gpt.app:app",
            host=host,
            port=port,
            reload=reload,
            log_level=log_level,
        )
        return 0
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
