from .metrics import router as metrics_router

def init_routes(app):
    app.include_router(metrics_router, prefix="/api/metrics")