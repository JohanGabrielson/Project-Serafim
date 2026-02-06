
from app.services.system import get_system_status
from app.logger import logger  
from app.services.system import restart_service, shutdown_service
from fastapi import APIRouter, HTTPException
import subprocess

router = APIRouter(prefix="/system", tags=["system"])

@router.post("/restart")
def restart():    
    subprocess.Popen(["sudo", "reboot"])
    return {"status": "restarting"}
   
@router.post("/shutdown")
def shutdown():  
    subprocess.Popen(["sudo", "shutdown", "-h", "now"])
    return {"status": "shutting_down"}
    


@router.get("/")
def system_status():
    logger.info("GET /system/ called")
    return get_system_status()


@router.get("")
def system_status_no_slash():
    logger.info("GET /system called")
    return get_system_status()