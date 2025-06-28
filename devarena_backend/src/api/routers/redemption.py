"""Reward/Redemption service endpoints."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.get("/", summary="Reward catalog", description="List rewards available for redemption.")
async def reward_catalog():
    return {"rewards": []}


# PUBLIC_INTERFACE
@router.post("/{reward_id}", summary="Redeem reward", description="Redeem a reward using credits.")
async def redeem_reward(reward_id: str):
    return {"reward_id": reward_id, "message": "Reward redeemed"}
