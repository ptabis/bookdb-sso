from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from app.classes.UserClass import User
from app.classes.TokenClass import Token
from app.models.TokenModel import TokenResponse
from app.models.RegisterModel import RegisterResponse

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User()
    if user.authenticate(form_data.username, form_data.password):
        token = Token()
        data = token.create_token({"username": form_data.username})
    else:
        data = ""
    response = JSONResponse(content={"access_token": data, "token_type": "bearer"})
    response.set_cookie(key="access_token", value=data)
    return response


@router.post("/register")
def register(username: str, password: str):
    user = User()
    return JSONResponse(content={"success": user.register(username, password)})
