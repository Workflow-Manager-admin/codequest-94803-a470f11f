"""Rule engine endpoints: View/configure code review rules."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.get("/", summary="List rules", description="Get list of quality and review rules.")
async def list_rules():
    return {"rules": []}


# PUBLIC_INTERFACE
@router.post("/", summary="Create/update rules", description="Create or update a rule.")
async def upsert_rule():
    return {"message": "Rule created/updated"}
