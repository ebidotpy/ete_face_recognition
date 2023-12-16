from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLlchemy_DATABASE_URL = "postgresql://postgres:09189498169@localhost/FaceRecognition"

engine = create_engine(
    SQLlchemy_DATABASE_URL
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()