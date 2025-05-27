# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     DATABASE_HOST: str
#     DATABASE_NAME: str
#     DATABASE_USER: str
#     DATABASE_PASSWORD: str
#     DATABASE_PORT: int
#     APP_NAME: str = "Full Stack To Do App"

#     class Config:
#         env_file = ".env"
#         extra = "ignore"

# settings = Settings()

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env

class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    APP_NAME: str = "Full Stack To Do App"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()