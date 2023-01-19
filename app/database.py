from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

db_host = os.environ['DATABASE_HOST']
db_port = os.environ['DATABASE_PORT']
db_username = os.environ['DATABASE_USERNAME']
db_password = os.environ['DATABASE_PASSWORD']
db_name = os.environ['DATABASE_NAME']
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()