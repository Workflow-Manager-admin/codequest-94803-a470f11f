"""
DevArena Backend Main Entrypoint

Handles application startup, API initialization, routing, security middlewares,
integrations, and documentation for DevArena's modular services.

This backend covers:
- PR handling and rule engine
- Bug logging and disputes
- Gamification, credits, leaderboards, and redemption
- User profiles and analytics
- Integrations (GitHub, GitLab, Bitbucket, Jira, Trello, Slack, Discord, SonarQube)
- Notifications, audit, rate limiting, and reviewer bias detector
- RESTful endpoints for frontend and webhooks for integrations

Swagger/OpenAPI docs: available at /docs
"""

import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from dotenv import load_dotenv
import uvicorn

# Module routers (to be implemented modularily)
from .routers import (
    auth, user_profiles, pull_requests, rules, bugs, disputes, gamification, leaderboard,
    redemption, notifications, integrations, audit, webhooks,
)
from .services.audit_trail import save_audit_log
from .utils.rate_limit_key import rate_limit_key_func

openapi_tags = [
    {"name": "Auth", "description": "SSO OAuth2 login and user session endpoints"},
    {"name": "UserProfile", "description": "User profile, settings, XP and achievements"},
    {"name": "PullRequests", "description": "Repository, PR, review, rule engine endpoints"},
    {"name": "Bugs", "description": "Peer bug/issue reporting and logs"},
    {"name": "Disputes", "description": "Dispute raising, voting, and resolution"},
    {"name": "Gamification", "description": "Credit, XP, levels, badges, achievements"},
    {"name": "Leaderboard", "description": "Leaderboard, rankings, analytics"},
    {"name": "Redemption", "description": "Reward redemption and store"},
    {"name": "Notifications", "description": "User and system notifications"},
    {"name": "Integrations", "description": "Git, Jira, Slack, Discord integrations"},
    {"name": "Audit", "description": "Audit trail and event logs"},
    {"name": "Webhooks", "description": "Webhooks for PRs, bots, notifications"},
]

# Load environment variables from .env (if exists)
load_dotenv()


# Create FastAPI app
app = FastAPI(
    title="DevArena Backend",
    description=(
        "API service for DevArena PR gamification, rule management, peer review, bug logging, "
        "disputes, credit/XP system, leaderboards, user profiles, rewards, analytics, and "
        "third-party integrations."
    ),
    version="1.0.0",
    openapi_tags=openapi_tags,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Set up CORS, Session, HTTPS redirect, Rate limiting, and more
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("CORS_ALLOW_ORIGINS", "*")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    SessionMiddleware, secret_key=os.getenv("SESSION_SECRET", "devarena_secret")
)
if os.getenv("FORCE_HTTPS", "0") == "1":
    app.add_middleware(HTTPSRedirectMiddleware)


@app.on_event("startup")
async def startup_event():
    # Initialize Redis for FastAPILimiter and sessions
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    await FastAPILimiter.init(redis_url)
    # Additional startup hooks, connection pools, etc.


# API Routers (Modular with tags)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user_profiles.router, prefix="/users", tags=["UserProfile"])
app.include_router(pull_requests.router, prefix="/prs", tags=["PullRequests"])
app.include_router(rules.router, prefix="/rules", tags=["PullRequests"])
app.include_router(bugs.router, prefix="/bugs", tags=["Bugs"])
app.include_router(disputes.router, prefix="/disputes", tags=["Disputes"])
app.include_router(gamification.router, prefix="/gamification", tags=["Gamification"])
app.include_router(leaderboard.router, prefix="/leaderboard", tags=["Leaderboard"])
app.include_router(redemption.router, prefix="/rewards", tags=["Redemption"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
app.include_router(integrations.router, prefix="/integrations", tags=["Integrations"])
app.include_router(audit.router, prefix="/audit", tags=["Audit"])
app.include_router(webhooks.router, prefix="/webhooks", tags=["Webhooks"])


# Global Rate Limiting: Default 100 req/min per user/IP
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    limiter = RateLimiter(times=100, seconds=60, key_func=rate_limit_key_func)
    await limiter(request)
    response = await call_next(request)
    return response


# Audit trail: Log all API calls except docs and root health
class AuditTrailMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if not request.url.path.startswith(("/docs", "/openapi.json", "/redoc")):
            await save_audit_log(request)
        response = await call_next(request)
        return response


app.add_middleware(AuditTrailMiddleware)


@app.get("/", tags=["Health"])
def health_check():
    """PUBLIC_INTERFACE
    Health check endpoint
    """
    return {"status": "ok", "message": "DevArena backend healthy"}


# PUBLIC_INTERFACE
@app.get(
    "/websockets_info",
    tags=["Webhooks"],
    summary="Websockets Usage",
    description="WebSocket usage info for integrations/notifications.",
)
def websockets_usage_docs():
    """
    Returns details on connecting to available websocket endpoints
    for real-time notifications and events.
    """
    return {
        "message":
            "WebSocket endpoints (docs example). To receive real-time notifications connect to "
            "ws(s)://<host>/ws/notifications or /ws/live_leaderboard"
    }


if __name__ == "__main__":
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
