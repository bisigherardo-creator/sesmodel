import os
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/analyze")
def analyze(
    trustpilot_url: str = Query(...),
    weight_sense: float = Query(0.2),
    weight_emotions: float = Query(0.3),
    weight_sentiments: float = Query(0.5),
):
    if round(weight_sense + weight_emotions + weight_sentiments, 2) != 1.0:
        return JSONResponse(
            status_code=400,
            content={"error": "I pesi devono sommare a 1"},
        )

    # Stub temporaneo
    scores = {
        "sense": -60,
        "emotions": -70,
        "sentiments": -80,
    }

    ses_index = (
        scores["sense"] * weight_sense
        + scores["emotions"] * weight_emotions
        + scores["sentiments"] * weight_sentiments
    )

    return {
        "trustpilot_url": trustpilot_url,
        "weights": {
            "sense": weight_sense,
            "emotions": weight_emotions,
            "sentiments": weight_sentiments,
        },
        "scores": scores,
        "ses_index": round(ses_index, 2),
    }
