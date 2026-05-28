from fastapi import APIRouter

from app.dependencies import metrics_service
from app.models.request_models import MetricsScoreRequest
from app.models.response_models import MetricsScoreResponse


router = APIRouter()


@router.post("/metrics/score", response_model=MetricsScoreResponse)
def score_metrics(payload: MetricsScoreRequest) -> MetricsScoreResponse:
    return metrics_service.score(payload)

