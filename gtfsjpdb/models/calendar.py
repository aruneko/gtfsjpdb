from sqlalchemy import Column, String, Boolean, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship

from gtfsjpdb.models.base import Base


class Calendar(Base):
    filename = 'calendar.txt'
    __tablename__ = 'calendar'

    id = Column(String(255), primary_key=True, nullable=False)
    monday = Column(Boolean, nullable=False)
    tuesday = Column(Boolean, nullable=False)
    wednesday = Column(Boolean, nullable=False)
    thursday = Column(Boolean, nullable=False)
    friday = Column(Boolean, nullable=False)
    saturday = Column(Boolean, nullable=False)
    sunday = Column(Boolean, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    trips = relationship("Trip", back_populates="calendar")
    calendar_dates = relationship("CalendarDate", back_populates="calendar")


class CalendarDate(Base):
    filename = 'calendar_dates.txt'
    __tablename__ = 'calendar_date'

    id = Column(Integer, primary_key=True)
    service_id = Column(String(255), ForeignKey("calendar.id"), nullable=False)
    service = relationship('Calendar', back_populates='calendar_dates')
    date = Column(Date, nullable=False)
    exception_type = Column(Integer, nullable=False)
