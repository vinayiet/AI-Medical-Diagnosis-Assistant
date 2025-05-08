from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = ''
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES = 30

def create_token(data: dict, expires_data: timedelta=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_data or timedelta(minutes=15))
    to_encode.update({"exp" : expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except JWTError:
        return None
