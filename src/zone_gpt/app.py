"""ZONE-GPT Core FastAPI Application Factory."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    """
    Create and configure the ZONE-GPT FastAPI application.

    Returns:
        FastAPI: Configured FastAPI application instance
    """
    app = FastAPI(
        title="ZONE-GPT Core API",
        version="1.0.0",
        description="Multi-agent business intelligence and operational management",
    )

    # Configure CORS for frontend connectivity
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, replace with your specific domain
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers
    from zone_gpt.routes import repo_routes

    app.include_router(repo_routes.router)

    return app


# Create application instance for uvicorn
app = create_app()
