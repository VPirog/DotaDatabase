from sqlalchemy import Column, Integer, Float, CHAR, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Guide(Base):
    __tablename__ = 'guide'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(99))
    rating = Column(Float)
    comment = Column(CHAR(99))
    owner_user_id = Column(ForeignKey('user.id'))
    hero_id = Column(ForeignKey('hero.id'))

    guides = relationship("ItemGuide", back_populates="guide")
    guideS_rating = relationship("UserRating", back_populates="guide_rating")
