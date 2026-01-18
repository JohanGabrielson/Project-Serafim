from fastapi import APIRouter
from app.services.system import get_system_status

router = APIRouter(prefix="/system", tags=["system"])

@router.get("/")
def system_status():
    return get_system_status()


@router.get("")
def system_status_no_slash():
    return get_system_status()