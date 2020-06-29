"""Sales router module."""
from fastapi import APIRouter


router = APIRouter()  # pylint: disable=invalid-name


@router.get('/')
async def get_people():
    """Get people endpoint."""

    return []
