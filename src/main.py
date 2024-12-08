from fastapi import FastAPI
from src.routers.AuthRouter import router as auth_router

app = FastAPI(title="Excel Processing")

app.include_router(auth_router)
