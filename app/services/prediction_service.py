import pandas as pd

from app.core.model_loader import load_model
from app.services.preprocessing_service import preprocess_input_data


def predict_fraud(data: pd.DataFrame):

    processed_data = preprocess_input_data(data)

    model = load_model()

    predictions = model.predict(processed_data)

    probabilities = model.predict_proba(processed_data)

    results = []

    for pred, prob in zip(predictions, probabilities):

        confidence = max(prob) * 100

        results.append(
            {
                "prediction":
                    "Fraud"
                    if pred == 1
                    else "Not Fraud",

                "confidence":
                    round(confidence, 2)
            }
        )

    return results