
from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Infrastructure"])
async def health_check():
    return {"status": "healthy", "model_loaded": False}
