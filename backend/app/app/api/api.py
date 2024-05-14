from fastapi import APIRouter

from app.api.api_v1.endpoints.digit import digit_api_router
from app.api.api_v1.endpoints.font import font_api_router

api_router = APIRouter(prefix="/api")
api_router.include_router(font_api_router, prefix="/font", tags=["utils"])
api_router.include_router(digit_api_router, prefix="/digit", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
