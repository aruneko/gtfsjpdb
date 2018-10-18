from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class Trip(Base):
    filename = 'trips.txt'
    __tablename__ = 'trip'

    route_id = Column(String(255), ForeignKey("route.id"))
    route = relationship('Route', back_populates='trips')
    service_id = Column(String(255), ForeignKey("service.id"))
    service = relationship('Service', back_populates='trips')
    id = Column(String(255), primary_key=True, nullable=False)
    headsign = Column(String(255))
    short_name = Column(String(255))
    direction_id = Column(Integer)
    block_id = Column(String(255))
    shape_id = Column(String(255), ForeignKey("shape.id"))
    shape = relationship('Shape', back_populates='trips')
    wheelchair_accesible = Column(Integer)
    bikes_allowed = Column(Integer)
    desc = Column(String(255))
    desc_symbol = Column(String(15))
    office_id = Column(String(255), ForeignKey("office.id"))
    office = relationship('Office', back_populates='trips')
