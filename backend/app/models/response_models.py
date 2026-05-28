from pydantic import BaseModel


class GenerateResponse(BaseModel):
    case_id: str
    summary: str
    checklist: list[str]
    suggested_questions: list[str]
    safety_label: str


class ReviewApproveResponse(BaseModel):
    case_id: str
    status: str


class MetricsScoreResponse(BaseModel):
    participant_id: str
    condition: str
    score_percent: float
    details: dict[str, float]

