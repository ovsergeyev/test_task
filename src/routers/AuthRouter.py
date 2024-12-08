from fastapi import APIRouter, Response, HTTPException
from src.schemas.SUser import SUser
from src.schemas.SAccessToken import SAccessToken
from src.auth import authenticate_user, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
async def login_user(response: Response, user_data: SUser):
    user = authenticate_user(user_data.username)
    if not user or user["password"] != user_data.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token: SAccessToken = create_access_token({"sub": str(user["username"])})
    response.set_cookie(
        "access_token",
        token.access_token,
        httponly=True,
        expires=token.expire,
        samesite="Lax",  # если https и кросс-доменные запросы в "None"
        secure=False,  # если https надо в True
    )
    return token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("access_token", httponly=True, samesite="None", secure=True)
