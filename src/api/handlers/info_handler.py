from fastapi import APIRouter

from src.api.models.basic import Info

router = APIRouter()


@router.get("/info", response_model=Info)
async def get_info() -> Info:
    """get info about endpoints"""
    return Info()
