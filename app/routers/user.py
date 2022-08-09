from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
import re

from app.models import crud, schemas
from app.db import get_db

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 

@router.put("/v1/create")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/v1/validation")
def create_user(user_input: int | str, db: Session = Depends(get_db)):
    if user_input is str:
        if re.search(regex,user_input):  
            user = crud.get_user_by_email(user_input)
        else: 
            raise HTTPException(status_code=400, detail="not valid email")
    if user_input is int:
        user = crud.get_user_by_phone(user_input)
    if user is None:
        return JSONResponse(status_code=200, content = user_input)
    else:
        user_out = user.first_name + user.last_name
        return JSONResponse(status_code=200, content = user_out)