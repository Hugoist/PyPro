from typing import final, Dict, Any
from abc import ABC, abstractmethod


@final
class Config:
    """Configuration class that cannot be inherited"""
    DATABASE_URL: str = "sqlite:///:memory:"
    MAX_CONNECTIONS: int = 10


# Abstract base class
class BaseRepository(ABC):
    """Abstract base repository defining the interface for saving data"""

    @abstractmethod
    def save(self, data: Dict[str, Any]) -> None:
        """Save data to the repository"""
        pass


# Concrete implementation of BaseRepository
class SQLRepository(BaseRepository):
    """SQL repository that implements saving data"""

    def save(self, data: Dict[str, Any]) -> None:
        """Save the data (simulated)"""
        print(f"Saving data to SQL database: {data}")


# tests
repo = SQLRepository()
repo.save({"name": "Product1", "price": 10.5})
