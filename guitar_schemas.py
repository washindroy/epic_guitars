from pydantic import BaseModel


class Guitar(BaseModel):
    id:int
    brand:str
    name:str
    finish:str
    price:float

class InsertGuitar(BaseModel):
    brand:str
    name:str
    finish:str
    price:float
