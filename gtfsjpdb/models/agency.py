from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class Agency(Base):
    filename = "agency.txt"
    __tablename__ = "agency"

    id = Column(String(255), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    timezone = Column(String(31), nullable=False)
    lang = Column(String(7))
    phone = Column(String(31))
    fare_url = Column(String(255))
    email = Column(String(255))
    agency_jp = relationship("AgencyJP", uselist=False, back_populates="agency")
    routes = relationship("Route", back_populates="agency")


class AgencyJP(Base):
    filename = "agency_jp.txt"
    __tablename__ = "agency_jp"

    id = Column(Integer, primary_key=True)
    agency_id = Column(String(255), ForeignKey("agency.id"))
    agency = relationship("Agency", back_populates="agency_jp")
    official_name = Column(String(255))
    zip_number = Column(String(255))
    address = Column(String(255))
    president_pos = Column(String(255))
    president_name = Column(String(255))
