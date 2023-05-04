from sqlalchemy import Column, Integer, Float, CHAR
from sqlalchemy.orm import relationship

from database import Base


class Item(Base):
    __tablename__ = 'item'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(50))
    price = Column(Integer)
    strenght = Column(Integer)
    agility = Column(Integer)
    intelligence = Column(Integer)
    health = Column(Integer)
    mana = Column(Integer)
    hp_regen = Column(Float)
    mana_regen = Column(Float)
    armor = Column(Integer)
    evasion = Column(Integer)
    magic_resistance = Column(Integer)
    spell_amp = Column(Integer)
    damage = Column(Integer)
    attack_speed = Column(Integer)
    movement_speed = Column(Integer)
    item_type = Column(CHAR(16))

    items = relationship("ItemGuide", back_populates="item")

    def __str__(self):
        return f"Айтем {self.id}: {self.name}"
