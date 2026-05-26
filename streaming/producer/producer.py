import json
import pandas as pd

from kafka import KafkaProducer


TOPIC_NAME = "medicare_claims"


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Loading dataset...")

df = pd.read_csv(
    "data/raw/TRAIN2.csv",
    encoding="utf-8-sig"
)

print(f"Loaded {len(df)} records")

for _, row in df.head(10).iterrows():

    record = row.to_dict()

    record.pop("PotentialFraud", None)

    producer.send(TOPIC_NAME,value=record)
       
print("10 records sent successfully")

producer.flush()

producer.close()