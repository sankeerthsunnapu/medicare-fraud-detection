import pandas as pd

from app.services.prediction_service import predict_fraud

df = pd.read_csv(
    "data/raw/TRAIN2.csv",
    encoding="utf-8-sig"
)

sample_df = df.head(5)

predictions = predict_fraud(sample_df)

print("\nPredictions:\n")

for i, pred in enumerate(predictions, start=1):
    print(f"Record {i}: {pred}")