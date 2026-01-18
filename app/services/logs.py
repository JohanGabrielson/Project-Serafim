import os

LOG_FILE = "/var/log/syslog"

def get_logs(lines: int = 200):
    if not os.path.exists(LOG_FILE):
        return {"error": f"Log file not found: {LOG_FILE}"}

    with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
        content = f.readlines()

    return {
        "file": LOG_FILE,
        "lines": lines,
        "data": content[-lines:]
    }