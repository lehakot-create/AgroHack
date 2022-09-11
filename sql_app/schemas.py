from pydantic import BaseModel


class ItemCoord(BaseModel):
    id: int
    lat: int
    lon: int
    height: int
    rainny: int
    nitrogen: int
    sunny: int
    transport: int
