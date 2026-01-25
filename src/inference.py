"""Inference utilities and cold-start handling (starter).

Expose functions for generating top-k recommendations given a model and user id.
"""

from typing import Any, List


def recommend(model: Any, user_id: int, k: int = 10) -> List[int]:
    """Return top-k item ids for a user. Placeholder implementation."""
    # Replace with model.predict or nearest-neighbors call
    return []


if __name__ == "__main__":
    print("inference module — hook up to saved models for real recommendations.")
