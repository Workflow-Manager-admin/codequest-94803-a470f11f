"""Gamification service endpoints: credit, XP, badges."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.get("/xp", summary="Get XP/credits", description="Fetch credits, XP, badge info for user.")
async def get_xp():
    return {"xp": 0, "credits": 0}


# PUBLIC_INTERFACE
@router.get("/badges", summary="User badges", description="List of level badges.")
async def get_badges():
    return {"badges": []}
