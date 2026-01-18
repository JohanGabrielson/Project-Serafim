from fastapi import APIRouter
from app.services.system import get_system_status

router = APIRouter(prefix="/status", tags=["status"])

@router.get("/")
def status():
    return get_system_status()

import platform
import os
from datetime import datetime

@router.get("/system")
def system_status():
    return {
        "uptime": "45h 11m 26s",  # ← du kan ersätta med riktig funktion om du vill
        "version": "1.0.0",
        "commit": "local",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "os": platform.system() + " " + platform.release(),
        "kernel": platform.version(),
        "load": os.getloadavg()
    }