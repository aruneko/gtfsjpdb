from geoalchemy2 import Geometry
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class Zone(Base):
    filename = 'stops.txt'
    __tablename__ = 'zone'
    id = Column(String(255), primary_key=True, nullable=False)

    stops = relationship("Stop", back_populates="zone")
    origin = relationship('FareRule', back_populates='origin_zone')
    destination = relationship('FareRule', back_populates='destination_zones')
    contains = relationship('FareRule', back_populates='contains_zones')


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
    parent_station_id = Column(String(255), ForeignKey('stop.id'))
    parent_station = relationship("Stop", back_populates="parent_stops")
    timezone = Column(String(31))
    wheelchair_boarding = Column(Integer)

    stop_time = relationship('StopTime', back_populates='stop')
    from_stop = relationship('Transfer', back_populates='from_stop')
    to_stop = relationship('Transfer', back_populates='to_stop')
