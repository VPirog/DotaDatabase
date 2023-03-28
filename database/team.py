from sqlalchemy import Column, Integer, Float, CHAR
from sqlalchemy.orm import relationship

from database import Base

class Team(Base):
    __tablename__ = 'team'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(99), nullable=False)
    divison = Column(Integer, nullable=False)
    region = Column(CHAR(20), nullable=False)

    teams = relationship("TeamTournament", back_populates="team")
