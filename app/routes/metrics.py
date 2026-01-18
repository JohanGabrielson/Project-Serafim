from fastapi import APIRouter
from app.services.system import get_cpu_usage, get_ram_usage, get_disk_usage

router = APIRouter()

@router.get("/cpu")
def cpu():
    return {"cpu_percent": get_cpu_usage()}

@router.get("/ram")
def ram():
    return get_ram_usage()

@router.get("/disk")
def disk():
    return get_disk_usage()