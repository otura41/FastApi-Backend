import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Esto facilita el uso de la base de datos en tus rutas FastAPI:

# from sqlalchemy.orm import Session
# from fastapi import Depends

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()