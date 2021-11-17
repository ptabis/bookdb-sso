from pydantic import BaseModel


class RegisterResponse(BaseModel):
    success: bool
