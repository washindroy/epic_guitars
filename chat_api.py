from fastapi import APIRouter
from openai_services import Convo

chat_router=APIRouter(prefix="/chat")

@chat_router.post("/")
def chat(message:str):
    response=Convo(message)

    return{"response":response.content}

