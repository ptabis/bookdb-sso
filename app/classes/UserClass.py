from passlib.context import CryptContext
import redis
from app.utils.config import config


class User:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    redis_client = redis.Redis(
        host=config.datasources.redis.host, port=config.datasources.redis.port, db=0
    )

    def authenticate(self, username: str, password: str) -> bool:
        hashed_password = self.redis_client.get(username)
        return self.verify_password(password, hashed_password)

    def register(self, username: str, password: str) -> bool:
        try:
            print(self.redis_client.get(username) is not None)
            if self.redis_client.get(username) is None:
                self.redis_client.set(username, self.get_password_hash(password))
            else:
                return False
        except Exception:
            return False

        return True

    def verify_password(self, plain_password, hashed_password) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password) -> str:
        return self.pwd_context.hash(password)
