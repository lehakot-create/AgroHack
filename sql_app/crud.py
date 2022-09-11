from sqlalchemy.orm import Session

from . import models


def get_dot(db: Session, lat: int):
    return db.query(models.Coords).filter(models.Coords.lat == lat).first()


def create_dot(db: Session, lat, lon, height, rainny, nitrogen, sunny, transport):
    db_dot = models.Coords(lat=lat,
                           lon=lon,
                           height=height,
                           rainny=rainny,
                           nitrogen=nitrogen,
                           sunny=sunny,
                           transport=transport)
    db.add(db_dot)
    db.commit()
    db.refresh(db_dot)
    return db_dot
