"""Application entry point.

Run locally with:
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI

from app.routers import patient

app = FastAPI(title="Patient Insights API", version="1.0.0")

app.include_router(patient.router)


@app.get("/health", tags=["meta"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
