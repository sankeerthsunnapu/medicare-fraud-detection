import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    roc_auc_score
)
from sklearn.model_selection import train_test_split

from app.core.config import (
    TRAIN_FILE,
    MODEL_PATH,
    FEATURE_COLUMNS_PATH
)

from app.services.preprocessing_service import preprocess_input_data


print("Loading dataset...")

df = pd.read_csv(TRAIN_FILE, encoding="utf-8-sig")

df.columns = df.columns.str.replace("ï»¿", "")

y = df["PotentialFraud"].astype(int)

X = preprocess_input_data(df)

feature_columns = X.columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training Random Forest model...")

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Evaluating model...")

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)

roc_auc = roc_auc_score(y_test, y_prob)

print(f"Accuracy: {accuracy:.4f}")

print(f"ROC-AUC: {roc_auc:.4f}")

print("\nClassification Report:\n")

print(classification_report(y_test, y_pred))

print("Saving model...")

joblib.dump(model, MODEL_PATH)

joblib.dump(feature_columns, FEATURE_COLUMNS_PATH)

print("Model saved successfully!")