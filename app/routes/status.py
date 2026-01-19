from fastapi import APIRouter
from app.services.system import get_system_status
from app.logger import logger   # ← detta är filen du undrar över

import platform
import os
from datetime import datetime

router = APIRouter(prefix="/status", tags=["status"])


@router.get("/")
def status():
    logger.info("GET /status called")
    return get_system_status()


@router.get("/system")
def system_status():
    logger.info("GET /status/system called")
    return {
        "uptime": "45h 11m 26s",
        "version": "1.0.0",
        "commit": "local",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "os": platform.system() + " " + platform.release(),
        "kernel": platform.version(),
        "load": os.getloadavg()
    }