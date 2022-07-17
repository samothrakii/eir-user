"""
Base setting class
Checkout this link for more info: https://pydantic-docs.helpmanual.io/usage/settings
"""
from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_URI: str | None = None

    @validator("POSTGRES_URI", pre=True)
    def generate_pg_uri(cls, v: str | None, values: dict[str, str]) -> str:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER") or "127.0.0.1",
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
        fields = {
            "POSTGRES_SERVER": {"env": "POSTGRES_SERVER"},
            "POSTGRES_USER": {"env": "POSTGRES_USER"},
            "POSTGRES_PASSWORD": {"env": "POSTGRES_PASSWORD"},
            "POSTGRES_DB": {"env": "POSTGRES_DB"},
        }


settings = Settings()
