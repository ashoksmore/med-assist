from fastapi import APIRouter

from app.dependencies import azure_openai_service, case_repository, guardrails_service
from app.models.request_models import GenerateRequest
from app.models.response_models import GenerateResponse
from app.services.prompt_builder import build_generation_prompt


router = APIRouter()


@router.post("/generate", response_model=GenerateResponse)
async def generate(payload: GenerateRequest) -> GenerateResponse:
    prompt = build_generation_prompt(payload)
    artifact = await azure_openai_service.generate_patient_artifact(payload.case_id, prompt)
    guarded = guardrails_service.apply(artifact)
    case_repository.save_case_output(payload.case_id, guarded.model_dump())
    return guarded

