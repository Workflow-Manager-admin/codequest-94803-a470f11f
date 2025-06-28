"""Pull requests/repository endpoints."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.get("/", summary="List PRs/repos", description="List pull requests for the user/repos.")
async def list_prs():
    return {"prs": []}


# PUBLIC_INTERFACE
@router.get("/{pr_id}", summary="Get PR details", description="Details for a pull request.")
async def get_pr(pr_id: str):
    return {"pr_id": pr_id, "status": "pending"}
