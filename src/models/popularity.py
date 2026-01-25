"""Popularity-based recommender: a simple baseline using item popularity.
The code below are randomly generated and need modification per requirements
"""
from typing import List
import pandas as pd

class PopularityRecommender:
    def __init__(self, top_k: int = 10):
        self.top_k = top_k
        self.popular_items = []

    def fit(self, interactions: pd.DataFrame, item_col: str = "item_id"):
        # interactions: DataFrame with at least item_id column
        counts = interactions[item_col].value_counts()
        self.popular_items = counts.index.tolist()

    def recommend(self, user_id: int, k: int = None) -> List[int]:
        k = k or self.top_k
        return self.popular_items[:k]
