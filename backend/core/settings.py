from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn

    model_config = SettingsConfigDict(env_file="backend/.env", extra="ignore")

settings = Settings()
