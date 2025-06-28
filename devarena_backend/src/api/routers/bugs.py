"""Bug/issue logging endpoints."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.post("/", summary="Log a bug", description="Report a bug/issue for PR.")
async def log_bug():
    return {"message": "Bug logged"}


# PUBLIC_INTERFACE
@router.get("/", summary="List bugs", description="Get bugs/issues reported by user/peers.")
async def list_bugs():
    return {"bugs": []}
