from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class FareAttribute(Base):
    filename = "fare_attributes.txt"
    __tablename__ = "fare_attribute"

    id = Column(String(255), primary_key=True, nullable=False)
    price = Column(Integer, nullable=False)
    currency_type = Column(String(3), nullable=False)
    payment_method = Column(Integer, nullable=False)
    transfers = Column(Integer)
    transfer_duration = Column(Integer)

    fare_rules = relationship('FareRule', back_populates='fare_attribute')


class FareRule(Base):
    filename = "fare_rules.txt"
    __tablename__ = "fare_rule"

    id = Column(Integer, primary_key=True)
    fare_id = Column(String(255), ForeignKey("fare_attribute.id"), nullable=False)
    fare_attribute = relationship('FareAttribute', back_populates='fare_rules')
    route_id = Column(String(255), ForeignKey("route.id"), nullable=False)
    route = relationship('Route', back_populates='fare_rules')
    origin_id = Column(String(255), ForeignKey("zone.id"), nullable=False)
    origin = relationship('Zone', back_populates='origin_fare_rules')
    destination_id = Column(String(255), ForeignKey("zone.id"), nullable=False)
    destination = relationship('Zone', back_populates='destination_fare_rules')
    contains_id = Column(String(255), ForeignKey("zone.id"), nullable=False)
    contains = relationship('Zone', back_populates='contains_fare_rules')
