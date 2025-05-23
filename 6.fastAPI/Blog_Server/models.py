from sqlalchemy import Column, Integer, String
from database import Base

class Blog(Base):
    __tablename__ = "blogs_table"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

class User(Base):
    __tablename__ = "users_table"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)