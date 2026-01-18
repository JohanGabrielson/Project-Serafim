import psutil
import time
import platform
import datetime
import subprocess
import os

def get_system_status():
    #Uptime  
    boot_time = psutil.boot_time()
    uptime_seconds = int(time.time() - boot_time)
    uptime_str = f"{uptime_seconds // 3600}h {(uptime_seconds % 3600) // 60}m {uptime_seconds % 60}s"

    return {
        "version": "1.0.0",
        "commit": "local",
        "uptime": uptime_str,
        "server_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "system": platform.system(),
        "release": platform.release(),
        "uptime_seconds": uptime_seconds,
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory": {
            "total": psutil.virtual_memory().total,
            "used": psutil.virtual_memory().used,
            "percent": psutil.virtual_memory().percent
        },
        "os": platform.system(),
        "kernel": platform.release(),
        "load": os.getloadavg(),

    }

def get_cpu_usage():
    return psutil.cpu_percent(interval=0.5)

def get_ram_usage():
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "used": memory.used,
        "percent": memory.percent
    }

def get_disk_usage():
    disk = psutil.disk_usage("/")

    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent": disk.percent
    }