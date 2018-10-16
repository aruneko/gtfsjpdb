from sqlalchemy import Column, Integer, String, Date

from gtfsjpdb.models.base import Base


class Feed(Base):
    filename = 'feed_info.txt'
    __tablename__ = 'feeds'

    id = Column(Integer, primary_key=True)
    publisher_name = Column(String(255), nullable=False)
    publisher_url = Column(String(255), nullable=False)
    lang = Column(String(255), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    version = Column(String(255))
    license = Column(String(255))
