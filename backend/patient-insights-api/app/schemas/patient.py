"""Pydantic request/response schemas for patient insights."""

from typing import Any

from pydantic import BaseModel, Field


class PatientInsightsRequest(BaseModel):
    patient_data: dict[str, Any] = Field(
        ...,
        description="Raw synthetic patient payload to summarize and question-generate.",
    )


class PatientSummary(BaseModel):
    patient_id: str
    name: str
    age: int
    chief_complaint: str
    active_conditions: list[str]
    current_medications: list[str]
    notable_findings: list[str]
    summary: str


class ProbableQuestion(BaseModel):
    question: str
    rationale: str


class ProbableQuestionsResponse(BaseModel):
    patient_id: str
    probable_questions: list[ProbableQuestion]


class PatientInsightsResponse(BaseModel):
    patient_summary: PatientSummary
    probable_questions: ProbableQuestionsResponse

