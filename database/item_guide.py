from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class ItemGuide(Base):
    __tablename__ = 'item_guide'
    __table_args__ = {'extend_existing': True}

    guide_id = Column('guide_id', ForeignKey('guide.id'), nullable=False),
    item_id = Column('item_id', ForeignKey('item.id'))

    item = relationship("Item", back_populates="items")
    guide = relationship("Guide", back_populates="guides")
