from geoalchemy2 import Geometry
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class Shape(Base):
    filename = "shapes.txt"
    __tablename__ = "shape"

    id = Column(String(255), primary_key=True, nullable=False)
    line = Column(Geometry("LINESTRING"), nullable=False)

    trip = relationship("Trip", back_populates="shapes")
