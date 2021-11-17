from datetime import datetime, timedelta
from jose import JWTError, jwt


class Token:
    SECRET_KEY = "968DDC93E2192399ACD991E0270AF10873D3043D9C44247F4F94A02306A1E40E"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 180

    def create_token(self, *data):
        data = data[0]
        access_token_expires = timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.utcnow() + access_token_expires
        data.update({"exp": expire})
        return jwt.encode(data, self.SECRET_KEY, algorithm=self.ALGORITHM)
