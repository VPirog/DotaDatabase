from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class TeamTournament(Base):
    __tablename__ = 'team_tournament'
    __table_args__ = {'extend_existing': True}

    team_id = Column(ForeignKey('team.id'), primary_key=True, nullable=False)
    tournament_id = Column(ForeignKey('tournament.id'), primary_key=True, nullable=False)

    team = relationship("Team", back_populates="teams")
    tournament = relationship("Tournament", back_populates="tournaments")

