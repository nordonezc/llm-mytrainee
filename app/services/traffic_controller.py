import os
import asyncio
from fastapi import HTTPException

class TrafficController:
    def __init__(self):
        self.max_concurrent = int(os.getenv("MAX_CONCURRENT_REQUESTS", "1"))
        self.max_queue_size = int(os.getenv("MAX_QUEUE_SIZE", "10"))
        self.request_timeout = float(os.getenv("REQUEST_TIMEOUT", "60"))
        
        self._semaphore = asyncio.Semaphore(self.max_concurrent)
        self._current_queue_count = 0

    async def run_with_limit(self, request_id: str, coro_func, *args):
        """Run a coroutine function with concurrency and queue limits."""
        if self._current_queue_count >= self.max_queue_size:
            print(f"[{request_id}] ERROR: Queue limit reached.")
            raise HTTPException(status_code=503, detail="Server overloaded.")

        self._current_queue_count += 1
        try:
            async with asyncio.timeout(self.request_timeout):
                async with self._semaphore:
                    return await coro_func(*args)
        except asyncio.TimeoutError:
            print(f"[{request_id}] ERROR: Timeout.")
            raise HTTPException(status_code=504, detail="Timeout reached.")
        finally:
            self._current_queue_count -= 1