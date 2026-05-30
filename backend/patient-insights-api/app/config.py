"""Application configuration.

Azure credentials are read from environment variables (or a local .env file)
rather than hard-coded. They are surfaced to the LLM service layer as plain
arguments at construction time — see app/dependencies.py.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    azure_openai_endpoint: str
    azure_openai_api_key: str
    azure_openai_deployment: str = "gpt-4o"
    azure_openai_api_version: str = "2024-10-21"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
