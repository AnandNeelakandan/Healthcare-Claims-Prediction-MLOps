from fastapi import APIRouter, HTTPException, Path
from db_models import get_member_by_id

router = APIRouter(prefix="/members", tags=["Members"])

@router.get("/{member_id}")
def get_member(
    member_id: str = Path(..., example="M2003")
):
    result = get_member_by_id(member_id)
    if not result:
        raise HTTPException(status_code=404, detail="Member not found")
    return result
