from sqlalchemy import Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class Frequency(Base):
    filename = "frequencies.txt"
    __tablename__ = "frequency"

    id = Column(Integer, primary_key=True)
    trip_id = Column(String(255), ForeignKey("trip.id"), nullable=False)
    trip = relationship("Trip", back_populates="frequencies")
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    headway_secs = Column(Integer, nullable=False)
    exact_times = Column(Integer)
