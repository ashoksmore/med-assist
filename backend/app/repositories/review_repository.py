class ReviewRepository:
    def __init__(self) -> None:
        self._reviews: dict[str, dict] = {}

    def save_review(self, case_id: str, payload: dict) -> None:
        self._reviews[case_id] = payload

    def get_review(self, case_id: str) -> dict | None:
        return self._reviews.get(case_id)

