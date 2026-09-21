from fastapi import FastAPI

from guitars_apis import guitars_router

app = FastAPI()

app.include_router(guitars_router)
