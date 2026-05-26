import pandas as pd

from app.core.model_loader import load_model
from app.services.preprocessing_service import preprocess_input_data


def predict_fraud(data: pd.DataFrame):

    processed_data = preprocess_input_data(data)

    model = load_model()

    predictions = model.predict(processed_data)

    prediction_labels = [
        "Fraud" if pred == 1 else "Not Fraud"
        for pred in predictions
    ]

    return prediction_labels