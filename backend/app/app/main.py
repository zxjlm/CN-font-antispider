from fastapi import FastAPI

from .api.api import api_router
from .core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
# if settings.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

app.include_router(api_router, prefix=settings.API_V1_STR)


# @app.middleware("http")
# def validate_token(headers):
#     """
#     验证第三方服务的 token
#     """
#     pass


@app.get("/test")
async def test():
    return {"foo": "bar"}
