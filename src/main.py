from fastapi import FastAPI
from src.routers.AuthRouter import router as auth_router
from src.routers.FileProcessingRouter import router as processing_router

app = FastAPI(title="Excel Processing")

app.include_router(auth_router)
app.include_router(processing_router)
