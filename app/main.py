from fastapi import FastAPI
from app.api import recommend_api

app = FastAPI()
app .include_router(recommend_api.router)
