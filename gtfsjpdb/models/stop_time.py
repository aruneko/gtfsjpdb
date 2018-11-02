from sqlalchemy import Column, Integer, String, ForeignKey, Time, Float
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class StopTime(Base):
    filename = "stop_times.txt"
    __tablename__ = "stop_time"

    id = Column(Integer, primary_key=True)
    trip_id = Column(String(255), ForeignKey("trip.id"), nullable=False)
    trip = relationship("Trip", back_populates="stop_times")
    arrival_time = Column(Time, nullable=False)
    departure_time = Column(Time, nullable=False)
    stop_id = Column(String(255), ForeignKey("stop.id"), nullable=False)
    stop = relationship("Stop", back_populates="stop_times")
    sequence = Column(Integer, nullable=False)
    headsign = Column(String(256))
    pickup_type = Column(Integer)
    drop_off_type = Column(Integer)
    shape_dist_traveled = Column(Float)
    timepoint = Column(Integer)
