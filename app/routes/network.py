from fastapi import APIRouter
from app.services.network import get_network_info

router = APIRouter(prefix="/network", tags=["network"])

@router.get("/")
def network():
    return get_network_info()