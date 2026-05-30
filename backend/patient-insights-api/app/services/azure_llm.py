"""Azure LLM Service Layer.

A thin, reusable wrapper around Azure OpenAI. The class is constructed with the
connection details (endpoint, API key, deployment, API version) and exposes a
single async method `generate(prompt, patient_data)` that returns parsed JSON.

Design notes:
- `prompt` becomes the system message; `patient_data` becomes the user message.
  Both are passed in by the caller, exactly as the task requires.
- `response_format={"type": "json_object"}` forces the model to emit valid JSON,
  so callers can rely on getting a dict back.
- The async client is used so FastAPI request handlers don't block the event
  loop while waiting on the network.
"""

import json
from typing import Any

from openai import AsyncAzureOpenAI


class AzureLLMService:
    def __init__(
        self,
        endpoint: str,
        api_key: str,
        deployment: str,
        api_version: str,
    ) -> None:
        self.deployment = deployment
        self._client = AsyncAzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            api_version=api_version,
        )

    async def generate(self, prompt: str, patient_data: Any) -> dict:
        """Send a prompt + data payload to the model and return parsed JSON.

        Args:
            prompt: Instruction text used as the system message.
            patient_data: A dict (or anything JSON-serialisable) sent as the
                user message. Strings are passed through untouched.

        Returns:
            The model's response parsed into a dict.

        Raises:
            ValueError: if the model returns content that is not valid JSON.
        """
        user_content = (
            patient_data
            if isinstance(patient_data, str)
            else json.dumps(patient_data)
        )

        response = await self._client.chat.completions.create(
            model=self.deployment,
            response_format={"type": "json_object"},
            temperature=0.2,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_content},
            ],
        )

        content = response.choices[0].message.content or ""
        try:
            return json.loads(content)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Model did not return valid JSON: {content[:200]}"
            ) from exc
