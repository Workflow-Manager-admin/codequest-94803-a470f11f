"""Auth endpoints: OAuth2/Social SSO, user session."""
from fastapi import APIRouter, Request, Query

router = APIRouter()


# PUBLIC_INTERFACE
@router.get(
    "/login",
    summary="OAuth Login",
    description="Start OAuth2 SSO login process for GitHub/GitLab/Bitbucket."
)
async def login(
    provider: str = Query(..., description="oauth_provider: github/gitlab/bitbucket"),
):
    # Placeholder for actual SSO redirect
    return {"message": f"Redirect to {provider} OAuth"}


# PUBLIC_INTERFACE
@router.get(
    "/callback",
    summary="OAuth Callback",
    description="OAuth2 callback endpoint after auth of provider."
)
async def oauth_callback(request: Request, provider: str):
    # Handle code exchange & issue JWT/session
    # Placeholder implementation
    return {"message": f"Callback received for {provider}"}


# PUBLIC_INTERFACE
@router.post(
    "/logout",
    summary="Logout",
    description="End user session/logout."
)
async def logout():
    # End user session/token
    return {"message": "Logged out"}
