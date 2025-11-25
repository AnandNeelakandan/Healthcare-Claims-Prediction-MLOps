from fastapi import APIRouter, HTTPException
from db.db_models import get_claim_by_id

router = APIRouter(prefix="/claims", tags=["Claims"])

@router.get("/{claim_id}")
def get_claim(claim_id: str):
    result = get_claim_by_id(claim_id)
    if not result:
        raise HTTPException(status_code=404, detail="Claim not found")
    return result

