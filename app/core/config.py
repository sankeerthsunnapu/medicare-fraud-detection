import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")

MODEL_DIR = os.path.join(BASE_DIR, "models")

LOG_DIR = os.path.join(BASE_DIR, "logs")

TRAIN_FILE = os.path.join(RAW_DATA_DIR, "TRAIN2.csv")
TEST_FILE = os.path.join(RAW_DATA_DIR, "TEST.csv")

MODEL_PATH = os.path.join(MODEL_DIR, "fraud_model.pkl")
FEATURE_COLUMNS_PATH = os.path.join(MODEL_DIR, "feature_columns.pkl")

PREDICTION_LOG_FILE = os.path.join(LOG_DIR, "predictions.csv")