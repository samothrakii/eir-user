from typing import Generator
import pytest

from app.db import get_db


@pytest.fixture(scope="session")
def session() -> Generator:
    yield get_db()
