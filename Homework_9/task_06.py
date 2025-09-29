from typing import List, Tuple, Union, TypeVar, TypedDict, Protocol, Optional, Dict, Generic, Callable


# task_01
def calculate_discount(price: float, discount: float) -> float:
    """
    Calculate discount based on price and discount
    """
    if discount > 100:
        return 0
    return price * (1 - discount / 100)


# tests
print(calculate_discount(100, 20))  # 80.0
print(calculate_discount(50, 110))  # 0.0


# task_02
def filter_adults(people: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Returns list of people older than 18 years
    """
    return list(filter(lambda p: p[1] >= 18, people))


# tests
people = [("Андрій", 25), ("Олег", 16), ("Марія", 19), ("Ірина", 15)]
print(filter_adults(people))

# [("Андрій", 25), ("Марія", 19)]


# task_04
T = TypeVar('T')


def parse_input(data: Union[int, str]) -> Union[int, None]:
    """
    Parsing integer from data input. Returns None if data isn't an integer
    """
    try:
        parsed_data = int(data)
    except ValueError:
        parsed_data = None

    return parsed_data


# tests
print(parse_input(42))  # 42
print(parse_input("100"))  # 100
print(parse_input("hello"))  # None


# task_05
def get_first(data: List[T]) -> Union[T, None]:
    """
    Returns first element of list or None if list is empty
    """
    return data[0] if len(data) else None


# tests
print(get_first([1, 2, 3]))  # 1
print(get_first(["a", "b", "c"]))  # "a"
print(get_first([]))  # None


# task_07
class User(TypedDict):
    id: int
    name: str
    is_admin: bool


class UserDatabase(Protocol):
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by id"""

    def save_user(self, user: User) -> None:
        """Save user to database"""


class InMemoryUserDB(UserDatabase):
    def __init__(self) -> None:
        self._users: Dict[int, User] = {}

    def get_user(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)

    def save_user(self, user: User) -> None:
        self._users[user["id"]] = user


if __name__ == "__main__":
    db = InMemoryUserDB()
    db.save_user({"id": 1, "name": "Alice", "is_admin": False})
    print(db.get_user(1))  # {"id": 1, "name": "Alice", "is_admin": False}
    print(db.get_user(2))  # None


# task_08
T = TypeVar("T")


class Processor(Generic[T]):
    def __init__(self, data: List[T]) -> None:
        self.data = data

    def apply(self, func: Callable[[T], T]) -> List[T]:
        """Apply a callable function to each element of the data list and return the result"""
        return [func(x) for x in self.data]


def double(x: int) -> int:
    return x * 2


def to_upper(s: str) -> str:
    return s.upper()


# tests
if __name__ == "__main__":
    p1 = Processor([1, 2, 3])
    print(p1.apply(double))  # [2, 4, 6]

    p2 = Processor(["hello", "world"])
    print(p2.apply(to_upper))  # ["HELLO", "WORLD"]


# task_09
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
