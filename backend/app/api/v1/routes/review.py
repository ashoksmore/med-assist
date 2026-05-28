from fastapi import APIRouter

from app.dependencies import review_service
from app.models.request_models import ReviewApproveRequest
from app.models.response_models import ReviewApproveResponse


router = APIRouter()


@router.post("/review/approve", response_model=ReviewApproveResponse)
def approve_review(payload: ReviewApproveRequest) -> ReviewApproveResponse:
    return review_service.approve(payload)

