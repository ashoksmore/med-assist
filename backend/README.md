# MedAssist Backend

FastAPI backend scaffold for the MedAssist prototype.

## Quick Start

1. Create a virtual environment.
2. Install dependencies:
   - `pip install -e .`
3. Copy env file:
   - `cp .env.example .env`
4. Run the API:
   - `uvicorn app.main:app --reload --port 8000`

## Endpoints

- `GET /api/v1/health`
- `POST /api/v1/generate`
- `POST /api/v1/review/approve`
- `POST /api/v1/metrics/score`

## Notes

- This scaffold uses in-memory placeholders, not a database.
- Add production persistence later by implementing the repository layer.
