from typing import Literal

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    case_id: str = Field(..., description="Synthetic case identifier")
    age_band: Literal["young_adult", "adult", "senior"]
    note_text: str = Field(..., min_length=20)


class ReviewApproveRequest(BaseModel):
    case_id: str
    approved: bool
    reviewer_notes: str = ""
    edited_summary: str | None = None
    edited_questions: list[str] | None = None


class MetricsScoreRequest(BaseModel):
    participant_id: str
    condition: Literal["raw", "plain"]
    answers: dict[str, str]

