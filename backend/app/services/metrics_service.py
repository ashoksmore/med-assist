from app.models.request_models import MetricsScoreRequest
from app.models.response_models import MetricsScoreResponse


class MetricsService:
    def score(self, payload: MetricsScoreRequest) -> MetricsScoreResponse:
        # Placeholder scoring logic.
        # Replace with rubric-based scoring from evaluation-protocol.md.
        score_percent = 80.0 if payload.condition == "plain" else 60.0
        return MetricsScoreResponse(
            participant_id=payload.participant_id,
            condition=payload.condition,
            score_percent=score_percent,
            details={"placeholder_score": score_percent},
        )

