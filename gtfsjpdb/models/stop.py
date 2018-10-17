from geoalchemy2 import Geometry
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class Zone(Base):
    __tablename__ = 'zone'
    id = Column(String(255), primary_key=True, nullable=False)
    stops = relationship("Stop", back_populates="zone")


class Stop(Base):
    filename = 'stops.txt'
    __tablename__ = 'stop'
    id = Column(String(255), primary_key=True, nullable=False)
    code = Column(String(255))
    name = Column(String(255), nullable=False)
    desc = Column(String(255))
    point = Column(Geometry('POINT'))
    zone_id = Column(String(255), ForeignKey('zone.id'))
    zone = relationship("Zone", back_populates="stops")
    url = Column(String(255))
    location_type = Column(Integer)
    parent_station = Column(String(255))
    timezone = Column(String(31))
    wheelchair_boarding = Column(Integer)
