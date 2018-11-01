from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class Office(Base):
    filename = 'office_jp.txt'
    __tablename__ = 'office'

    id = Column(String(255), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    url = Column(String(255))
    phone = Column(String(15))

    trip = relationship("Trip", back_populates="offices")
