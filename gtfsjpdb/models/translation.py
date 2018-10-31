from sqlalchemy import Column, Integer, String

from gtfsjpdb.models.base import Base


class Translation(Base):
    filename = "translations.txt"
    __tablename__ = "translation"

    id = Column(Integer, primary_key=True)
    trans_id = Column(String(255), nullable=False)
    lang = Column(String(3), nullable=False)
    translation = Column(String(255), nullable=False)
