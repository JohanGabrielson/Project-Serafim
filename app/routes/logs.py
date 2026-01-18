from fastapi import APIRouter
from app.services.logs import get_logs

router = APIRouter(prefix="/logs", tags=["logs"])

@router.get("/")
def logs():
    return get_logs()