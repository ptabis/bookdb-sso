from fastapi import FastAPI
from app.routers import default
from app.utils.config import config

if config.docker == 1:
    openapi_url = None
    docs_url = None
    redoc_url = None
else:
    openapi_url = "/openapi.json"
    docs_url = "/docs"
    redoc_url = "/redoc"


app = FastAPI(
    title="bookdb sso",
    version="0.1.0",
    openapi_url=openapi_url,
    docs_url=docs_url,
    redoc_url=redoc_url,
)

app.include_router(default.router)
