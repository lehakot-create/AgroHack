from pydantic import BaseModel


class ItemCoord(BaseModel):
    id: int
    lat: float
    lon: float
    height: int
    rainny: int
    nitrogen: int
    sunny: int
    transport: int
