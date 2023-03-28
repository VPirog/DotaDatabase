from sqlalchemy import Column, Integer, Float, CHAR, ForeignKey, Date
from sqlalchemy.orm import relationship

from database import Base


class ProPlayer(Base):
    __tablename__ = 'pro-player'
    __table_args__ = {'extend_existing': True}


    id = Column(Integer, primary_key=True)
    nickname = Column(CHAR(99), nullable=False)
    team_id = Column(ForeignKey('team.id'), nullable=False)
    user_id = Column(ForeignKey('user.id'), nullable=False)
    bday = Column(Date, nullable=False)
    role = Column(CHAR(20), nullable=False)

    team = relationship('Team')
    user = relationship('User')
