from fastapi import APIRouter

from src.api.models.basic import Root

router = APIRouter()


@router.get("/", response_model=Root)
async def root() -> Root:
    """get info about authors and group"""
    return Root()
