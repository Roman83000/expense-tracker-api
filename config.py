from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TOKEN_EXPIRE_MINUTES: int = 30
    SECRET_KEY: str
    DATABASE_URL: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()


