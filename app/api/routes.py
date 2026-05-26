import pandas as pd

from fastapi import APIRouter

from app.schemas.prediction_schema import PredictionResponse
from app.services.prediction_service import predict_fraud

router = APIRouter()


@router.get("/")
def health_check():
    return {
        "status": "running",
        "service": "Medicare Fraud Detection API"
    }


@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict():

    sample_data = pd.read_csv(
        "data/raw/TRAIN2.csv",
        encoding="utf-8-sig"
    ).head(1)

    prediction = predict_fraud(sample_data)[0]

    return PredictionResponse(
        prediction=prediction
    )