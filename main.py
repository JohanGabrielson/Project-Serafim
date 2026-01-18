from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# import routes
from app.routes.status import router as status_router
from app.routes.disk import router as disk_router
from app.routes.network import router as network_router
from app.routes.logs import router as logs_router
from app.routes.system import router as system_router
from app.routes.metrics import router as metrics_router

app = FastAPI(title="Serafim API") 

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"message": "Serafim API is running"}

app.include_router(system_router, prefix="/api")
app.include_router(status_router, prefix="/api")
app.include_router(disk_router, prefix="/api")
app.include_router(network_router, prefix="/api")
app.include_router(logs_router, prefix="/api")
app.include_router(metrics_router, prefix="/api/metrics")


