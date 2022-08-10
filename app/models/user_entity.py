from datetime import datetime
from enum import unique
from inspect import _empty
from queue import Empty
from sqlite3 import DateFromTicks
from pydantic import EmailStr
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship

from app.db import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    role_id = Column(Integer, ForeignKey("user_role.role_id"))
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date_of_birth = Column(Date)
    version = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class UserRole(Base):
    __tablename__ = "user_role"
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True, unique=True)
    role_id = Column(Integer, ForeignKey("role.id"), primary_key=True, unique=True)
    version = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    version = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
