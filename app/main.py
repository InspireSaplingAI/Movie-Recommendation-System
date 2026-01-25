"""FastAPI backend (starter).

Run with: uvicorn app.main:app --reload
"""

from fastapi import FastAPI

app = FastAPI(title="Movie Recommendation API")


@app.get("/")
async def health_check():
    return {"status": "ok"}


@app.get("/recommend/{user_id}")
async def recommend_endpoint(user_id: int, k: int = 10):
    # Placeholder: wire to real inference code
    return {"user_id": user_id, "recommendations": [], "k": k}
