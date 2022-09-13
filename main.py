from random import randrange

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from sql_app import crud, models
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['http://localhost:63342']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
def get_dot(lat: float, db: Session = Depends(get_db)):
    """
    В разработке
    :param lat:
    :param db:
    :return:
    """
    dot = crud.get_dot(db, lat=lat)
    return dot


@app.post('/dot/')
def post_dot(lat, lon, height, rainny, nitrogen, sunny, transport, db: Session = Depends(get_db)):
    """
    Позволяет создать новую точку с параметрами
    :param lat: широта
    :param lon: долгота
    :param height: Высота над уровнем моря
    :param rainny: Количество осадков в год
    :param nitrogen: Содержание азота в почве%
    :param sunny: Количество солнечных дней в году
    :param transport: Наличие транспортного сообщения
    :return:
    """
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


@app.post('/dots/')
def create_many_dots(lat: float = 43.585473, lon: float = 39.723093, step: float = 0.000001,
                     qty_dots: int = 2, db: Session = Depends(get_db)):
    """
    Заполняет БД фейковыми данными
    :param lat: широта 1.123456
    :param lon: долгота 1.123456
    :param step: шаг изменения долготы и широты
    :param qty_dots: количество точек по горизонтали
    :return:
    """
    latitude = lat
    for _ in range(qty_dots):
        longitude = lon
        for _ in range(qty_dots):
            crud.create_dot(db=db,
                            lat=latitude,
                            lon=longitude,
                            height=randrange(0, 5),
                            rainny=randrange(0, 5),
                            nitrogen=randrange(0, 3),
                            sunny=randrange(0, 3),
                            transport=randrange(0, 1))
            longitude += step
        latitude += step
    return 'ok'


@app.get('/all-dots/')
def get_all_dots(limit: int = 10, db: Session = Depends(get_db)):
    """
    Возвращает все точки
    :param limit: количество точек, если не указано, то 10
    :param db:
    :return:
    """
    return crud.get_all_dots(db=db).limit(limit).all()
