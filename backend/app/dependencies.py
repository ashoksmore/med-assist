from app.repositories.case_repository import CaseRepository
from app.repositories.review_repository import ReviewRepository
from app.services.azure_openai_service import AzureOpenAIService
from app.services.guardrails_service import GuardrailsService
from app.services.metrics_service import MetricsService
from app.services.review_service import ReviewService


case_repository = CaseRepository()
review_repository = ReviewRepository()
azure_openai_service = AzureOpenAIService()
guardrails_service = GuardrailsService()
review_service = ReviewService(review_repository)
metrics_service = MetricsService()

