import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.container import llm_service
from app.core.config import settings
from app.api.llm_api import router as chat_router
from app.api.health_api import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("--- [Lifecycle] Starting FastAPI ---")
    start_time = time.time()
    try:
        print(f"--- [Lifecycle] Loading model: {settings.model_id} ---")
        llm_service.engine.load_model()
        
        end_time = time.time()
        print(f"--- [Lifecycle] Model ready in {end_time - start_time:.2f} seconds ---")
    except Exception as e:
        print(f"--- [Lifecycle] Error loading model: {e} ---")
    
    yield
    print("--- [Lifecycle] Shutting down FastAPI ---")

def create_application() -> FastAPI:
    application = FastAPI(
        title="AI LLM API Service",
        description="MS to call LLMs and provide AI services to MyTrainee app",
        version="1.0.0",
        lifespan=lifespan
    )

    application.include_router(chat_router, prefix="/api/v1", tags=["Chat"])
    application.include_router(health_router, prefix="/api/v1", tags=["Infrastructure"])
    return application

app = create_application()

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )


    
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "message": str(exc)}
    )


