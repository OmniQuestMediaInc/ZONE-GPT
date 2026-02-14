"""Command-line interface for ZONE-GPT."""

import sys

import uvicorn


def main():
    """Main entry point for the ZONE-GPT CLI."""
    uvicorn.run("zone_gpt.app:app", host="0.0.0.0", port=8000, reload=True, log_level="info")


if __name__ == "__main__":
    sys.exit(main())
