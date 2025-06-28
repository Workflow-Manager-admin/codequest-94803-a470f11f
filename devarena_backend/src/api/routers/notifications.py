"""Notification endpoints: real-time and system notifications."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.get("/", summary="Fetch notifications", description="Get current user's notifications.")
async def get_notifications():
    return {"notifications": []}
