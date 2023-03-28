from sqlalchemy import Column, Integer, Float, CHAR
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(99))
    phone = Column(Integer)

    userS_rating = relationship("UserRating", back_populates="user_rating")
