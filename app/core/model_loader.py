import joblib
from app.core.config import MODEL_PATH

model = None


def load_model():
    global model

    if model is None:
        model = joblib.load(MODEL_PATH)

    return model