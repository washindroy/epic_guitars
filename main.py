from fastapi import FastAPI

from chat_api import chat_router
from guitars_apis import guitars_router

app = FastAPI()

app.include_router(guitars_router)
app.include_router(chat_router)
