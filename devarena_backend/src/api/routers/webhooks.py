"""Webhooks endpoints for bot/PR notifications."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.post(
    "/notifications",
    summary="Notification webhook",
    description="Webhook for notifications from integrations."
)
async def notification_webhook():
    return {"received": True}
