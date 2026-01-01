from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.groq_client import get_llm_response
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to Groq LLM Chat API"}

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    logger.info(f"Received chat request: {request.message}")
    try:
        reply = get_llm_response(request.message)
        logger.info(f"Generated reply: {reply}")
        return ChatResponse(reply=reply)
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error communicating with LLM: {str(e)}")
