from fastapi import APIRouter
from app.services.disk import get_disk_info

router = APIRouter(prefix="/disk", tags=["disk"])

@router.get("/")
def disk():
    return get_disk_info()