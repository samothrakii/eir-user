from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import crud, schemas, user_entity
from app.db import SessionLocal, engine, get_db

from app.routers import example
from app.core.config import settings

user_entity.Base.metadata.create_all(bind=engine)

app = FastAPI()

print(settings.POSTGRES_URI)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


app.include_router(example.router)


@app.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
