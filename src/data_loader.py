"""Data ingestion and preprocessing pipelines (starter).

This module should be expanded with dataset-specific loaders and preprocessing steps.
"""

import pandas as pd
from typing import Any


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(path)


def preprocess_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Simple placeholder preprocessing: drop NA and duplicate rows."""
    df = df.dropna().drop_duplicates()
    return df


if __name__ == "__main__":
    print("data_loader module loaded — replace with real pipelines.")
