import pandas as pd

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset


print("Loading datasets...")

reference_data = pd.read_csv(
    "data/raw/TRAIN2.csv",
    encoding="utf-8-sig"
)

current_data = pd.read_csv(
    "data/raw/TEST.csv",
    encoding="utf-8-sig"
)

# Remove target column if present
if "PotentialFraud" in reference_data.columns:
    reference_data = reference_data.drop(
        columns=["PotentialFraud"]
    )

# Keep only common columns
common_columns = list(
    set(reference_data.columns)
    & set(current_data.columns)
)

reference_data = reference_data[common_columns]

current_data = current_data[common_columns]

print(
    f"Comparing {len(common_columns)} common features..."
)

print("Generating drift report...")

report = Report(
    metrics=[
        DataDriftPreset()
    ]
)

report.run(
    reference_data=reference_data,
    current_data=current_data
)

report.save_html(
    "monitoring/drift_reports/data_drift_report.html"
)

print(
    "Drift report generated successfully!"
)