from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def hello():
    return "Hello from FastAPI"


@app.get('/dot/')
def get_dot(lat: int, db: Session = Depends(get_db)):
    dot = crud.get_dot(db, lat=lat)
    return dot


@app.post('/dot/')
def post_dot(lat, lon, height, rainny, nitrogen, sunny, transport, db: Session = Depends(get_db)):
    db_dot = crud.get_dot(lat=lat, db=db)
    if db_dot:
        raise HTTPException(status_code=400, detail='Dot already exists')
    return crud.create_dot(db=db,
                           lat=lat,
                           lon=lon,
                           height=height,
                           rainny=rainny,
                           nitrogen=nitrogen,
                           sunny=sunny,
                           transport=transport)


# 43.585473, 39.723093
