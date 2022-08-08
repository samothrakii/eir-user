from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.models import user_entity
from app.db import SessionLocal, engine, get_db

from app.routers import user
from app.core.config import settings

user_entity.Base.metadata.create_all(bind=engine)

app = FastAPI()

print(settings.POSTGRES_URI)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


app.include_router(user.router)

