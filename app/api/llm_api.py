from fastapi import APIRouter, Depends
from app.schemas.chat_schema import ChatRequest
from app.services.llm_service import LLMService
from app.core.container import get_llm_service

router = APIRouter()

@router.post("/generate")
async def generate(
    chat_req: ChatRequest, 
    service: LLMService = Depends(get_llm_service)):
    return {"response": await service.get_response(chat_req.prompt)}