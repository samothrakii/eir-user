from typing import Generator
import pytest

from app.db.session import SessionLocal


@pytest.fixture(scope="session")
def session() -> Generator:
    yield SessionLocal()
