from app.models.request_models import ReviewApproveRequest
from app.models.response_models import ReviewApproveResponse
from app.repositories.review_repository import ReviewRepository


class ReviewService:
    def __init__(self, repository: ReviewRepository) -> None:
        self.repository = repository

    def approve(self, payload: ReviewApproveRequest) -> ReviewApproveResponse:
        status = "approved" if payload.approved else "needs_changes"
        self.repository.save_review(payload.case_id, payload.model_dump())
        return ReviewApproveResponse(case_id=payload.case_id, status=status)

