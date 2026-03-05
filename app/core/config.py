from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_id: str
    model_file: str
    model_type: str
    max_concurrent_requests: int = 1
    max_queue_size: int = 10
    request_timeout: float = 60.0
    max_generation_length: int
    context_length: int

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding='utf-8',
        extra='ignore')

@lru_cache()
def get_settings():
    """ 
    Singleton to ensure settings are loaded only once. 
    """
    return Settings()

settings = get_settings()