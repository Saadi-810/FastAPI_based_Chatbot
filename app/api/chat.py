from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.groq_client import get_llm_response


router=APIRouter()

@router.get("/")
def read_root():
    return {"message":"Welcome to Groq LLM Chat API"}


@router.post("/chat", response_model=ChatResponse)
def chat(request:ChatRequest):
    reply=get_llm_response(request.message)
    return ChatResponse(reply=reply)