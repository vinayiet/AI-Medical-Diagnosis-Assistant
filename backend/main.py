# This is the entry point of the backend
from fastapi import FastAPI
from api.routes import router
app = FastAPI()
app.include_router(router)
