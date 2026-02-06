from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

# import routes
from app.routes.status import router as status_router
from app.routes.disk import router as disk_router
from app.routes.network import router as network_router
from app.routes.logs import router as logs_router
from app.routes.system import router as system_router
from app.routes.metrics import router as metrics_router

# import logger
from app.logger import logger

app = FastAPI(title="Serafim API")



from fastapi.responses import FileResponse

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
  #  logger.info("GET / called")
  #return {"message": "Serafim API is running"}
    return FileResponse("static/index.html")

# register routers
app.include_router(system_router, prefix="/api")
app.include_router(status_router, prefix="/api")
app.include_router(disk_router, prefix="/api")
app.include_router(network_router, prefix="/api")
app.include_router(logs_router, prefix="/api")
app.include_router(metrics_router, prefix="/api/metrics")


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        log_config=None  # Disable uvicorn's default logging
    )