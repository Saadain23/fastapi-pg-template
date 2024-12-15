import os
from dotenv import load_dotenv
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "GenMail"
    DATABASE_URL: str = str(os.getenv("DATABASE_URL"))
    SECRET_KEY: str = str(os.getenv("SECRET_KEY"))
    JWT_ALGO: str = str(os.getenv("ALGORITHM"))
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

settings = Settings()