from fastapi import APIRouter, Cookie, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from app.classes.UserClass import User
from app.classes.TokenClass import Token
from app.models.TokenModel import TokenResponse
from app.models.RegisterModel import RegisterResponse
from app.utils.basedir import BASE_DIR
from app.utils.config import config
from pathlib import Path
from typing import Optional

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
templates = Jinja2Templates(directory=str(Path(BASE_DIR, "templates")))


@router.get("/", response_class=HTMLResponse)
def home(request: Request, site: Optional[str] = None):
    return templates.TemplateResponse("login.html.jinja", {"request": request})


@router.post("/token", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User()
    if user.authenticate(form_data.username, form_data.password):
        token = Token()
        data = token.create_token({"username": form_data.username})
    else:
        data = None

    if data is not None:
        response = JSONResponse(content={"access_token": data, "token_type": "bearer"})
        response.set_cookie(key="access_token", value=data)
    else:
        response = JSONResponse()

    return response


@router.get("/authenticate")
def authenticate(
    request: Request, access_token: Optional[str] = Cookie(None), site: str = None
):
    referer = request.headers.get("referer")

    if referer == site and referer in config.hosts_whitelist:
        return RedirectResponse(f"{referer}/auth?token={access_token}")

    return RedirectResponse(f"/?site={referer}")


@router.get("/register", response_class=HTMLResponse)
def register_get(request: Request):
    return templates.TemplateResponse("register.html.jinja", {"request": request})


@router.post("/register")
def register(username: str, password: str):
    user = User()
    return JSONResponse(content={"success": user.register(username, password)})
