import logging

logging.basicConfig(
    filename="/var/log/serafim/backend.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("serafim")