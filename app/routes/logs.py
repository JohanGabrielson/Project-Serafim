import os
from fastapi import APIRouter
from app.services.logs import get_logs

LOG_PATH = "/var/log/serafim/backend.log"

def get_logs(max_lines=100):
    if not os.path.exists(LOG_PATH):
        return {"logs": ["Log file not found."]}
    try:
        with open(LOG_PATH, "r") as f:
            lines = f.readlines()
        lines = [line.strip("\n") for line in lines]
        return {"logs": lines[-max_lines:]}
    except Exception as e:
        return {"logs": [f"Error reading log: {e}"]}



router = APIRouter(prefix="/logs", tags=["logs"])

@router.get("/")
def read_logs():
    return get_logs()