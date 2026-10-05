from fastapi import APIRouter
from fastapi.responses import JSONResponse

from guitar_schemas import InsertGuitar
from guitars_repository import guitar_repository

guitars_router = APIRouter(prefix="/guitars")


@guitars_router.get("/")
def list_guitars(limit: int=10):
    return guitar_repository.get_guitars_list(limit=limit)


@guitars_router.post('/')
def create(new_guitar: InsertGuitar):
    guitar = guitar_repository.create_guitar(new_guitar)
    return JSONResponse({"guitar": guitar})


@guitars_router.put("/{guitar_id}")
def update_guitar(guitar_id: int, guitar: InsertGuitar):
    updated_guitar = guitar_repository.update_guitar(guitar_id, guitar)
    return {"guitar": updated_guitar}
 

@guitars_router.delete('/')
def delete(guitar_id: int):
    guitar_repository.delete_guitar(guitar_id=guitar_id)
    return JSONResponse(status_code=204)


@guitars_router.get("/{guitar_id}")
def get_guitar(guitar_id: int):
    guitar = guitar_repository.get_guitar_details(guitar_id=guitar_id)
    return {"guitar": guitar}