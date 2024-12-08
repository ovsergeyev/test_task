from fastapi import Request, HTTPException, Depends
from typing import Union
from datetime import datetime, timedelta, timezone
from src.schemas.SAccessToken import SAccessToken
import jwt
from jwt import InvalidTokenError
from src.config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

fake_users = [{"username": settings.LOGIN, "password": settings.PASSWORD}]


def authenticate_user(username):
    found_users = list(filter(lambda user: user["username"] == username, fake_users))
    user = found_users[0] if found_users else None
    return user


def create_access_token(
    data: dict, expires_delta: Union[timedelta, None] = None
) -> SAccessToken:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return SAccessToken(access_token=encoded_jwt, expire=expire, token_type="jwt")


def get_access_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Absent token")
    return token


def get_current_user(access_token: str = Depends(get_access_token)):
    try:
        payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Incorrect token format")

    expire: str = payload.get("exp")
    if not expire or (int(expire) < datetime.now(timezone.utc).timestamp()):
        raise HTTPException(status=401, detail="Token expired")
    username: str = payload.get("sub")
    if not username:
        raise HTTPException(status=401)

    user = authenticate_user(username)

    if not user:
        raise HTTPException(status=401)

    return user
