from sqlalchemy import Column, Integer, String
from app.db import Base


class Example(Base):
    __tablename__ = "example"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    def __init__(self, name: str, *args, **kwargs):
        self.name = name
