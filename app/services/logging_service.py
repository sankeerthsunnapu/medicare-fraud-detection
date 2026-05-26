import os
import pandas as pd

from datetime import datetime

from app.core.config import PREDICTION_LOG_FILE


def log_prediction(
    provider,
    prediction
):

    log_entry = pd.DataFrame([
        {
            "timestamp": datetime.now(),
            "provider": provider,
            "prediction": prediction
        }
    ])

    if os.path.exists(PREDICTION_LOG_FILE):

        log_entry.to_csv(
            PREDICTION_LOG_FILE,
            mode="a",
            header=False,
            index=False
        )

    else:

        log_entry.to_csv(
            PREDICTION_LOG_FILE,
            index=False
        )