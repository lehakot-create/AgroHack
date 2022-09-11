from sqlalchemy import Column, Integer

from .database import Base


class Coords(Base):
    __tablename__ = 'dots'

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Integer, unique=True, index=True)  # широта
    lon = Column(Integer, unique=True, index=True)  # долгота
    height = Column(Integer, unique=True, index=True)  # Высота над уровнем моря
    rainny = Column(Integer, unique=True, index=True)  # Количество осадков в год
    nitrogen = Column(Integer, unique=True, index=True)  # Содержание азота в почве%
    sunny = Column(Integer, unique=True, index=True)  # Количество солнечных дней в году
    transport = Column(Integer, unique=True, index=True)  # Наличие транспортного сообщения
