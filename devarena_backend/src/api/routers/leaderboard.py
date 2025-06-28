"""Leaderboard endpoints: rankings, analytics."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.get(
    "/", summary="Get leaderboard",
    description="Get leaderboard stats (weekly/monthly/all-time)."
)
async def leaderboard():
    return {"leaderboard": []}
