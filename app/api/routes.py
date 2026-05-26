import pandas as pd

from fastapi import APIRouter

from fastapi import UploadFile, File
from fastapi.responses import JSONResponse
import tempfile

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

    result = predict_fraud(sample_data)[0]

    return PredictionResponse(
        prediction=result["prediction"],
        confidence=result["confidence"]
    )

@router.post("/predict-file")
async def predict_file(
    file: UploadFile = File(...)
):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".csv"
    ) as temp_file:

        temp_file.write(await file.read())

        temp_file_path = temp_file.name

    df = pd.read_csv(
        temp_file_path,
        encoding="utf-8-sig"
    )

    results = predict_fraud(df)

    predictions = [
        r["prediction"]
        for r in results
    ]

    return JSONResponse(
        content={
            "total_records": len(predictions),
            "fraud_predictions": predictions.count("Fraud"),
            "non_fraud_predictions": predictions.count("Not Fraud")
        }
    )