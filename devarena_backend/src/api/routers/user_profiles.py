"""User profiles, settings, XP, badge endpoints."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.get("/", summary="Get user profile", description="Fetch current user's profile and stats.")
async def get_profile():
    return {"profile": "user profile info"}


# PUBLIC_INTERFACE
@router.put("/", summary="Update user profile", description="Update profile data/settings.")
async def update_profile():
    return {"message": "Profile updated"}
