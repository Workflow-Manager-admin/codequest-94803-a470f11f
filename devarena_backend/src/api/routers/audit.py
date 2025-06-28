"""Audit trail endpoints."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.get("/", summary="Audit logs", description="List of audit event logs.")
async def audit_logs():
    return {"logs": []}
