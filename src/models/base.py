"""Abstract base classes for recommenders."""
from abc import ABC, abstractmethod
from typing import List

class RecommenderBase(ABC):
    @abstractmethod
    def fit(self, data):
        raise NotImplementedError()

    @abstractmethod
    def recommend(self, user_id: int, k: int = 10) -> List[int]:
        raise NotImplementedError()
