from fastapi import APIRouter

router = APIRouter(prefix="/meta")

@router.get("/trends")
def meta_trends(format: str, archetype: str, window_days: int = 30):
    return {
        "status": "stub",
        "format": format,
        "archetype": archetype,
        "window_days": window_days
    }

