from fastapi import APIRouter, HTTPException, Path
from db.db_models import get_provider_by_npi

router = APIRouter(prefix="/providers", tags=["Providers"])

@router.get("/{provider_npi}")
def get_provider(
    provider_npi: str = Path(..., example="P0468")
):
    result = get_provider_by_npi(provider_npi)
    if not result:
        raise HTTPException(status_code=404, detail="Provider not found")
    return result
