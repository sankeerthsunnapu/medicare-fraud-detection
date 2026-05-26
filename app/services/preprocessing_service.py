import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.replace("ï»¿", "")
    return df


def preprocess_input_data(df: pd.DataFrame) -> pd.DataFrame:

    df = clean_column_names(df)

    if "Provider" in df.columns:
        df = df.drop(columns=["Provider"])

    if "PotentialFraud" in df.columns:
        df = df.drop(columns=["PotentialFraud"])

    return df