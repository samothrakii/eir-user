from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
import re

from app.models import crud, schemas
from app.db import get_db
from app.util import const

from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/v1/create", tags=["user"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/v1/validation", tags=["user"])
def validate_email_phone(user_input: str, db: Session = Depends(get_db)):
    user: schemas.User | None = None
    if re.search(const.email_regex,user_input):  
        user = crud.get_user_by_email(db=db , email=user_input)
    elif re.search(const.phone_number_regex,user_input):  
        user = crud.get_user_by_phone(db=db, phone_number=user_input)
    else: 
        raise HTTPException(status_code=400, detail="not valid email/phone number")

    if user is not None:
        return JSONResponse(status_code=409, content=None)
    else:
        return JSONResponse(status_code=200, content=None)
