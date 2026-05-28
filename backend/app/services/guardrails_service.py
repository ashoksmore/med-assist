from app.models.response_models import GenerateResponse


class GuardrailsService:
    def apply(self, artifact: GenerateResponse) -> GenerateResponse:
        # Minimal placeholder guardrail hook.
        # Add source-anchoring and unsupported-claim checks here.
        return artifact

