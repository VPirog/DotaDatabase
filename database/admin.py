from sqlalchemy import Column, Integer, Float, CHAR
from database import Base


class Admin(Base):
    __tablename__ = 'admin'
    __table_args__ = {'extend_existing': True}


    id = Column(Integer, primary_key=True)
    name = Column(CHAR(99), nullable=False)
    phone = Column(CHAR(20))