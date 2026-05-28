class CaseRepository:
    def __init__(self) -> None:
        self._cases: dict[str, dict] = {}

    def save_case_output(self, case_id: str, payload: dict) -> None:
        self._cases[case_id] = payload

    def get_case_output(self, case_id: str) -> dict | None:
        return self._cases.get(case_id)

