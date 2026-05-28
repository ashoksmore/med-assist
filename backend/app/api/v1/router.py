from fastapi import APIRouter

from app.api.v1.routes.generate import router as generate_router
from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.metrics import router as metrics_router
from app.api.v1.routes.review import router as review_router


api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
api_router.include_router(generate_router, tags=["generate"])
api_router.include_router(review_router, tags=["review"])
api_router.include_router(metrics_router, tags=["metrics"])

