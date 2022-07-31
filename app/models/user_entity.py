from enum import unique
from inspect import _empty
from queue import Empty
from sqlite3 import Date
from pydantic import EmailStr
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    role_id = Column(Integer, ForeignKey("user_role.role_id"))
    phone_number = Column(Integer, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    date_of_birth = Column(DateTime)
    version = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class UserRole(Base):
    __tablename__ = "user_role"
    user_id = Column(Integer, ForeignKey("user.id"))
    role_id = Column(Integer, ForeignKey("role.id"))
    version = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, _empty=False)
    version = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
