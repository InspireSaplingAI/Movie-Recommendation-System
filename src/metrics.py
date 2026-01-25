"""Evaluation metrics for recommender systems: Precision@K, Recall@K (starter).
"""
from typing import List


def precision_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
    recommended_k = recommended[:k]
    if not recommended_k:
        return 0.0
    hits = len(set(recommended_k) & set(relevant))
    return hits / len(recommended_k)


def recall_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
    if not relevant:
        return 0.0
    recommended_k = recommended[:k]
    hits = len(set(recommended_k) & set(relevant))
    return hits / len(relevant)
