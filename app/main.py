from fastapi import FastAPI

from app.routers import example
from app.core.config import settings


app = FastAPI()

print(settings.POSTGRES_URI)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


app.include_router(example.router)
