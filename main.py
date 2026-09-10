from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, field_validator, Field

class Guitar(BaseModel):
    id:int
    brand:str
    name:str
    finish:str 
    price:float 

    # @field_validator("price")
    # @classmethod
    # def validate_price(cls, value: float):
    #     if value <=0:
    #         raise ValueError('batata price is higher than 0.')
    #     return value




app = FastAPI()
guitars=[
     Guitar(id=1, brand="Gibson", name="70s Flying V", price=2499.00, finish="Classic White"),
     Guitar(id=2, brand="ESP", name="Snakebyte", finish="Snow White", price=1499.00),
     Guitar(id=3, brand="Shecter", name="Synyster Gates Custom-S", finish="Gloss Black with Silver Stripes", price=1599.00),
     Guitar(id=4, brand="Jackson", name="Rhoads JS32T", price=469.99, finish="White with Black Bevels"),
     Guitar(id=5, brand="Fender", name="Player II Stratocaster HSS", price=999.99, finish="Transparent Cherry Burst with Rosewood Fingerboard"),
     Guitar(id=6, brand="PRS", name="SE Studio", finish="Charcoal Cherry Burst", price=1099.00)
]    

# localhost:8000/guitars
@app.get('/')
def root():
    return('Welcome to Guitar Center')

@app.post('/guitars')
def create(guitar: Guitar):
    guitars.append(guitar)
    return guitars

@app.get("/gutiars")
def list_guitars(limit : int =10):
    return guitars[0:limit]

@app.put("/guitars/{guitar_id}")
def update_guitar(guitar_id: int, guitar: Guitar):
    for existing_guitar in guitars:
        if existing_guitar.id == guitar_id:
            existing_guitar.brand = guitar.brand
            existing_guitar.name = guitar.name
            existing_guitar.finish = guitar.finish
            existing_guitar.price = guitar.price

            return existing_guitar

    raise HTTPException(
        status_code=404,
        detail=f"guitar {guitar_id} not found"
    )




# @app.put("/guitars")
# def update_list(guitar:Guitar):
#      update=guitar.model_dump()
#      guitars=update
#      return {"updated"}
     

@app.delete('/guitars')
def delete(gutiar_id: int):
    deleted = guitars.pop(gutiar_id-1)
    print(f"deleted: {deleted}")
    return Response(status_code=204)

@app.get("/guitars/{guitar_id}")
def get_guitar(guitar_id: int):
    if 0 <=guitar_id < len(guitars):
        return guitars[guitar_id-1]
    else:
            raise HTTPException(status_code=404, detail=f"guitar {guitar_id} not found")
        
        
        



    # if 0 <=guitar_id < len(guitars):
    #     return guitars[guitar_id]
    # else:
    #     raise HTTPException(status_code=404, detail=f"guitar {guitar_id} not found")

    #for guitar in guitars:
    #     if guitar["id"]==guitar_id: