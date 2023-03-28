from sqlalchemy import Column, Integer, Float, CHAR, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Tournament(Base):
    __tablename__ = 'tournament'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    series = Column(CHAR(20))
    organizer = Column(CHAR(20))
    prize_pool = Column(Integer)
    numer_of_team = Column(SmallInteger)
    admin_id = Column(ForeignKey('admin.id'))

    admin = relationship('Admin')

    tournaments = relationship("TeamTournament", back_populates="tournament")
