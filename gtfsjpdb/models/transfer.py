from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class Transfer(Base):
    filename = "transfers.txt"
    __tablename__ = "transfer"

    id = Column(Integer, primary_key=True)
    from_stop_id = Column(String(255), ForeignKey("stop.id"), nullable=False)
    from_stop = relationship('Stop', back_populates='from_transfers')
    to_stop_id = Column(String(255), ForeignKey("stop.id"), nullable=False)
    to_stop = relationship('Stop', back_populates='to_transfers')
    transfer_type = Column(Integer, nullable=False)
    min_transfer_time = Column(Integer)
