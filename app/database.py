from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import json

database_secret_env = os.environ['RDS_SECRET']
print(database_secret_env)
database_secret = json.loads(database_secret_env)

db_host = database_secret['host']
db_port = database_secret['port']
db_username = database_secret['username']
db_password = database_secret['password']
db_name = database_secret['dbname']

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()