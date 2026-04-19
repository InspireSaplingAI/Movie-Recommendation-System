"""Evaluation metrics for recommender systems: Precision@K, Recall@K, RMSE, MAE (starter).
"""
from typing import List, Tuple
import numpy as np


def precision_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
    """Calculate Precision@K.
    
    Precision measures: of the top-K recommended items, how many are relevant?
    
    Args:
        recommended: List of recommended item IDs (in ranking order)
        relevant: List of relevant item IDs for the user
        k: Cutoff (consider only top-K recommendations)
    
    Returns:
        Precision@K score (0.0 to 1.0)
        
    TODO: Implement Precision@K
    Steps:
    1. Get only top-k recommendations: recommended_k = recommended[:k]
    2. If empty, return 0.0
    3. Count hits: len(set(recommended_k) & set(relevant))
    4. Return hits / len(recommended_k)
    """
    # YOUR CODE HERE
    pass


def recall_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
    """Calculate Recall@K.
    
    Recall measures: of all relevant items, how many appear in top-K?
    
    Args:
        recommended: List of recommended item IDs (in ranking order)
        relevant: List of relevant item IDs for the user
        k: Cutoff (consider only top-K recommendations)
    
    Returns:
        Recall@K score (0.0 to 1.0)
        
    TODO: Implement Recall@K
    Steps:
    1. Check if relevant is empty, return 0.0
    2. Get only top-k recommendations
    3. Count hits: len(set(recommended_k) & set(relevant))
    4. Return hits / len(relevant)
    """
    # YOUR CODE HERE
    pass


def mean_absolute_error(y_true: List[float], y_pred: List[float]) -> float:
    """Calculate Mean Absolute Error (MAE).
    
    Measures average absolute difference between predicted and true ratings.
    Useful for regression-style rating prediction.
    
    Args:
        y_true: True ratings
        y_pred: Predicted ratings
    
    Returns:
        MAE score
        
    TODO: Implement MAE
    Formula: mean(|y_true - y_pred|)
    Hint: Use np.mean() and np.abs()
    """
    # YOUR CODE HERE
    pass


def root_mean_squared_error(y_true: List[float], y_pred: List[float]) -> float:
    """Calculate Root Mean Squared Error (RMSE).
    
    Measures standard deviation of residuals. Penalizes larger errors more.
    Useful for rating prediction tasks.
    
    Args:
        y_true: True ratings
        y_pred: Predicted ratings
    
    Returns:
        RMSE score
        
    TODO: Implement RMSE
    Formula: sqrt(mean((y_true - y_pred)^2))
    Hint: Use np.sqrt(), np.mean(), and ** 2 for squaring
    """
    # YOUR CODE HERE
    pass


def ndcg_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
    """Calculate Normalized Discounted Cumulative Gain (NDCG@K).
    
    Considers ranking position: items ranked higher contribute more to the score.
    Items appear as 1 if relevant, 0 otherwise.
    
    Args:
        recommended: List of recommended item IDs (in ranking order)
        relevant: List of relevant item IDs for the user
        k: Cutoff
    
    Returns:
        NDCG@K score (0.0 to 1.0)
        
    TODO: Implement NDCG@K
    Steps:
    1. Get top-k recommendations, return 0.0 if empty or no relevant items
    2. Create a set of relevant items for O(1) lookup
    3. Calculate DCG (Discounted Cumulative Gain):
       - For each item at position i (starting from 1) in recommended_k:
         * If item is relevant: dcg += 1.0 / log2(i+1)
    4. Calculate IDCG (Ideal DCG):
       - All top-min(len(relevant), k) items are relevant
       - Sum: 1.0 / log2(i+1) for i from 1 to min(len(relevant), k)
    5. Return dcg / idcg (or 0.0 if idcg is 0)
    Hint: Use np.log2() for logarithm
    """
    # YOUR CODE HERE
    pass

