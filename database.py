from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Abc12345@127.0.0.1:3306/bjpowernode"  # 连接MySQL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass