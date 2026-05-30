"""Dependency wiring.

`get_llm_service` constructs the Azure LLM Service Layer from settings and is
cached so the underlying HTTP client is reused across requests. FastAPI injects
it into route handlers via `Depends`.
"""

from functools import lru_cache

from app.config import settings
from app.services.azure_llm import AzureLLMService


@lru_cache
def get_llm_service() -> AzureLLMService:
    return AzureLLMService(
        endpoint=settings.azure_openai_endpoint,
        api_key=settings.azure_openai_api_key,
        deployment=settings.azure_openai_deployment,
        api_version=settings.azure_openai_api_version,
    )
