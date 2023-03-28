from sqlalchemy import Column, Integer, Float, CHAR
from database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(99))
    phone = Column(Integer)