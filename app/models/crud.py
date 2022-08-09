from sqlalchemy.orm import Session

import app.models.user_entity as user_entity
import app.models.schemas as schemas

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = user_entity.User(email=user.email, phone_number=user.phone_number, first_name = user.first_name, last_name=user.last_name, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(user_entity.User).filter(user_entity.User.email == email).first()

def get_user_by_phone(db: Session, phone_number: int):
    return db.query(user_entity.User).filter(user_entity.User.phone_number == phone_number).first()
