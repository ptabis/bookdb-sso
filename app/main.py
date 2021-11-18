from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import default
from app.utils.config import config
from app.utils.basedir import BASE_DIR
from pathlib import Path

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

app.mount(
    "/static", StaticFiles(directory=str(Path(BASE_DIR, "static"))), name="static"
)

app.include_router(default.router)
