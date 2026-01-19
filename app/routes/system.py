from fastapi import APIRouter
from app.services.system import get_system_status
from app.logger import logger   # ← korrekt import

router = APIRouter(prefix="/system", tags=["system"])


@router.get("/")
def system_status():
    logger.info("GET /system/ called")
    return get_system_status()


@router.get("")
def system_status_no_slash():
    logger.info("GET /system called")
    return get_system_status()