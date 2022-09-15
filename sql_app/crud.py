from sqlalchemy.orm import Session

from . import models


def get_dot(db: Session, lat: float):
    return db.query(models.Coords).filter(models.Coords.lat == lat).first()


def get_all_dots(db: Session):
    return db.query(models.Coords)


def create_dot(db: Session, lat, lon, height, rainny, nitrogen, sunny, transport, content):
    db_dot = models.Coords(lat=lat,
                           lon=lon,
                           height=height,
                           rainny=rainny,
                           nitrogen=nitrogen,
                           sunny=sunny,
                           transport=transport,
                           content=content)
    db.add(db_dot)
    db.commit()
    db.refresh(db_dot)
    return db_dot
