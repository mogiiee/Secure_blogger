from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_DB_URL = "sqlite:///./users.db"

engine = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False})

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()
