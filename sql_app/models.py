from sqlalchemy import Column, Integer, Float

from .database import Base


class Coords(Base):
    __tablename__ = 'dots'

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float, unique=False, index=True)  # широта
    lon = Column(Float, unique=False, index=True)  # долгота
    height = Column(Integer, unique=False)  # Высота над уровнем моря 0-5
    rainny = Column(Integer, unique=False)  # Количество осадков в год 0-5
    nitrogen = Column(Integer, unique=False)  # Содержание азота в почве% 0-3
    sunny = Column(Integer, unique=False)  # Количество солнечных дней в году 0-3
    transport = Column(Integer, unique=False)  # Наличие транспортного сообщения 0-1
