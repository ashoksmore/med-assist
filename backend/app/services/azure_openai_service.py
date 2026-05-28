from app.models.response_models import GenerateResponse


class AzureOpenAIService:
    async def generate_patient_artifact(self, case_id: str, prompt: str) -> GenerateResponse:
        # Placeholder response until Azure API integration is added.
        # Keep this response stable so frontend integration can proceed.
        _ = prompt
        return GenerateResponse(
            case_id=case_id,
            summary="Draft plain-language summary placeholder.",
            checklist=[
                "Take medication as prescribed.",
                "Schedule and complete follow-up labs.",
                "Attend follow-up clinic appointment.",
            ],
            suggested_questions=[
                "What side effects should make me call the clinic?",
                "What should I do if I miss a dose?",
                "When should I repeat my blood tests?",
            ],
            safety_label="Conversation starters, not medical advice.",
        )

