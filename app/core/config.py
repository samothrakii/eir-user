"""
Base setting class
Checkout this link for more info: https://pydantic-docs.helpmanual.io/usage/settings
"""
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    pg_uri: PostgresDsn

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        fields = {"pg_uri": {"env": "POSTGRES_URI"}}


settings = Settings()
