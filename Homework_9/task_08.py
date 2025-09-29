from typing import TypeVar, Generic, List, Callable

# Generic type variable
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
