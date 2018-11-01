from sqlalchemy import Column, String, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class Route(Base):
    filename = 'routes.txt'
    __tablename__ = 'route'

    id = Column(String(255), primary_key=True, nullable=False)
    agency_id = Column(String(255), ForeignKey('agency.id'), nullable=False)
    agency = relationship('Agency', back_populates='routes')
    short_name = Column(String(255), nullable=False, default='')
    long_name = Column(String(255), nullable=False, default='')
    desc = Column(String(255))
    type = Column(Integer, nullable=False, default=3)
    url = Column(String(255))
    color = Column(String(7))
    text_color = Column(String(7))
    parent_route_id = Column(String(255))
    route_jp = relationship("RouteJP", uselist=False, back_populates="route")
    trips = relationship("Trip", back_populates="route")
    fare_rules = relationship("FareRule", back_populates="")


class RouteJP(Base):
    filename = 'routes_jp.txt'
    __tablename__ = 'route_jp'

    id = Column(Integer, primary_key=True)
    route_id = Column(String(255), ForeignKey("route.id"))
    route = relationship('Route', back_populates='route_jp')
    update_date = Column(Date)
    origin_stop = Column(String(255))
    via_stop = Column(String(255))
    destination_stop = Column(String(255))
