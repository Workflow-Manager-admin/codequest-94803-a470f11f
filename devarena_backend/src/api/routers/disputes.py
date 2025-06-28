"""Dispute resolution, peer voting endpoints."""
from fastapi import APIRouter

router = APIRouter()


# PUBLIC_INTERFACE
@router.post("/", summary="Raise dispute", description="Raise a dispute on review/bug.")
async def raise_dispute():
    return {"message": "Dispute registered"}


# PUBLIC_INTERFACE
@router.post("/{dispute_id}/vote", summary="Peer vote", description="Vote for dispute resolution.")
async def vote_dispute(dispute_id: str):
    return {"dispute_id": dispute_id, "result": "vote registered"}
