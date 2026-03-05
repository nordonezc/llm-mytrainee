import os
from ctransformers import AutoModelForCausalLM
from app.core.config import settings

class LLMEngine:
    def __init__(self):
        self.llm = None
        self.model_id = settings.model_id
        self.model_file = settings.model_file
        self.model_type = settings.model_type 
        
        self.cache_dir = "./models" 
        os.makedirs(self.cache_dir, exist_ok=True)
    
    def load_model(self):
        """Load the model. If not present, download it."""
        if self.llm is None:
            print(f"--- [Engine] Loading/Downloading model: {settings.model_id} ---")
            self.llm = AutoModelForCausalLM.from_pretrained(
                settings.model_id,
                model_file=settings.model_file,
                model_type=settings.model_type,
                context_length=settings.context_length
            )
            print("--- [Engine] Model loaded in RAM ---")

    def generate(self, prompt: str, temperature: float) -> str:
        """Synchronous method to generate response from the model."""
        return self.llm(prompt, temperature=temperature, max_new_tokens=settings.max_generation_length)