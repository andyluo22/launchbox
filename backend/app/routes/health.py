from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["heatlh"])
def health_check():
    """Simple Liveness Endpoint"""
    return {"status": "ok"}
