from app.models.request_models import GenerateRequest


def build_generation_prompt(payload: GenerateRequest) -> str:
    return (
        "You are creating patient-friendly output from a synthetic clinical note.\n"
        f"Age band: {payload.age_band}\n"
        "Return a plain summary, action checklist, and probable questions.\n"
        "Avoid unsupported claims.\n"
        f"Source note:\n{payload.note_text}"
    )

