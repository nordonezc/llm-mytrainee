from app.services.llm_service import LLMService

llm_service = LLMService()

def get_llm_service():
    return llm_service