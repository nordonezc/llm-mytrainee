import uuid
import anyio
from app.services.llm_engine import LLMEngine
from app.services.traffic_controller import TrafficController

class LLMService:
    def __init__(self):
        self.engine = LLMEngine()
        self.traffic = TrafficController()

    async def get_response(self, prompt: str, temperature: float = 0.7) -> str:
        request_id = str(uuid.uuid4())
        formatted_prompt = f"[INST] {prompt} [/INST]"

        print(f"[{request_id}] NEW REQUEST | Queue Position: {self.traffic._current_queue_count}")

        return await self.traffic.run_with_limit(
            request_id,
            self._execute_inference,
            formatted_prompt,
            temperature
        )

    async def _execute_inference(self, prompt: str, temperature: float) -> str:
        """Run the inference in a separate thread to avoid blocking the event loop."""
        return await anyio.to_thread.run_sync(
            self.engine.generate, 
            prompt, 
            temperature
        )