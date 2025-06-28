"""Integrations endpoints for Git/Jira/Trello/Slack/Discord connections."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.post(
    "/github/webhook",
    summary="GitHub webhook",
    description="Handle GitHub webhook events."
)
async def github_webhook():
    return {"event": "github received"}


# PUBLIC_INTERFACE
@router.post(
    "/slack/webhook",
    summary="Slack webhook",
    description="Slack bot integration."
)
async def slack_webhook():
    return {"event": "slack received"}
