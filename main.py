from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
import psycopg2

con=psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password='0000',
    host='localhost',
    port='5432'
)

cur=con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS guitars(
        id SERIAL PRIMARY KEY,
        brand VARCHAR,
        name VARCHAR,
        price NUMERIC,
        finish VARCHAR
    )
""")

cur.executemany("""
    INSERT INTO guitars(id, brand, name, price, finish)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING
""", [(1 ,'Gibson' ,'70s Flying V' ,2499.00 ,'Classic White' ),
(2 ,'ESP' ,'SnakeByte' ,1499.00 ,'Snow White' ),
(3 ,'Shecter' ,'Synyster Gates Custom-S' ,1599.00 ,'Gloss Black with Silver Stripes' ),
(4 ,'Jackson' ,'Rhoads JS32T' ,469.99 ,'White with Black Bevels' ),
(5 ,'Fender' ,'Player II Stratocaster HSS' ,999.99 ,'Transparent Cherry Burst with Rosewood Fingerboard' ),
(6 ,'PRS','SE Studio',1099.00 ,'Charcoal Cherry Burst'),
(7,'Fender', 'American Professional II jazzmaster', 1739.99, 'Dark Night with Rosewood Fingerboard'),
(8, 'Epiphone', 'SG Custom Electric Guitar', 699.00, 'Alpine White'),
(9,'Ibanez', 'Prestige RG652AHM', 1799.99, 'Antique White'),
(10,'ESP', 'Kirk Hammett Signature White Zombie', 1619.10, 'Black with Graphic')])




class Guitar(BaseModel):
    id:int
    brand:str
    name:str
    finish:str
    price:float


app = FastAPI()
cur.execute("SELECT id, brand, name, finish, price FROM guitars ORDER BY id")
guitars = [Guitar(id=row[0], brand=row[1], name=row[2], finish=row[3], price=row[4]) for row in cur.fetchall()]

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
        
con.commit()
cur.close()
con.close()
       
        





