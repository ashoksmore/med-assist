"""Patient insights route.

Pipeline:
  1. Accept patient JSON payload in request body.
  2. (patient data + PROMPT1) -> Azure LLM -> Patient Summary (JSON).
  3. (Patient Summary + PROMPT2) -> Azure LLM -> Patient Probable Questions (JSON).
  4. Validate shapes with Pydantic and return structured response.
"""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError

from app.dependencies import get_llm_service
from app.prompts.prompts import PROMPT1, PROMPT2
from app.schemas.patient import (
    PatientInsightsRequest,
    PatientInsightsResponse,
    PatientSummary,
    ProbableQuestionsResponse,
)
from app.services.azure_llm import AzureLLMService

router = APIRouter(prefix="/patients", tags=["patients"])

@router.post("/insights", response_model=PatientInsightsResponse)
async def get_patient_insights(
    payload: PatientInsightsRequest,
    llm: AzureLLMService = Depends(get_llm_service),
) -> PatientInsightsResponse:
    """Generate patient summary and probable questions from input JSON payload."""
    patient_data = payload.patient_data

    try:
        # Step 1: raw patient data -> Patient Summary
        patient_summary_raw = await llm.generate(PROMPT1, patient_data)
        patient_summary = PatientSummary.model_validate(patient_summary_raw)

        # Step 2: Patient Summary -> Patient Probable Questions
        probable_questions_raw = await llm.generate(PROMPT2, patient_summary.model_dump())
        probable_questions = ProbableQuestionsResponse.model_validate(probable_questions_raw)
    except ValidationError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Model response failed schema validation: {exc.errors()}",
        )
    except ValueError as exc:
        # Raised when the model returns non-JSON content.
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    except Exception as exc:  # noqa: BLE001 - surface upstream/Azure failures
        raise HTTPException(status_code=502, detail=f"LLM request failed: {exc}") from exc

    return PatientInsightsResponse(
        patient_summary=patient_summary,
        probable_questions=probable_questions,
    )
