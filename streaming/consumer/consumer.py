import json
import pandas as pd

from kafka import KafkaConsumer

from app.services.logging_service import log_prediction

from app.services.prediction_service import predict_fraud


TOPIC_NAME = "medicare_claims"


consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="fraud-consumer-group",
    value_deserializer=lambda x: json.loads(
        x.decode("utf-8")
    )
)

print("Fraud Prediction Consumer Started...")


for message in consumer:

    record = message.value

    df = pd.DataFrame([record])

    result = predict_fraud(df)[0]

    prediction = result["prediction"]

    confidence = result["confidence"]

    log_prediction(
    provider=record.get("Provider"),
    prediction=prediction
    )


    print("\n========================")

    print(f"Provider: {record.get('Provider')}")

    print(f"Prediction: {prediction}")

    print(f"Confidence: {confidence}%")
    
    print("========================")