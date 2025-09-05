from __future__ import annotations

from typing import List


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __lt__(self, other: Person) -> bool:
        return self.age < other.age

    def __gt__(self, other: Person) -> bool:
        return self.age > other.age

    def __eq__(self, other: Person) -> bool:
        return self.age == other.age

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def sorted_persons(persons: List[Person]) -> List[Person]:
    return sorted(persons)


p1 = Person("Oleksandr", 35)
p2 = Person("Dmytro", 36)
p3 = Person("Serhii", 34)

print(p1)  # Person(name=Oleksandr, age=35)
print(p2)  # Person(name=Dmytro, age=36)
print(p3)  # Person(name=Serhii, age=34)

print(sorted_persons(
    [p1, p2, p3]))  # [Person(name=Serhii, age=34), Person(name=Oleksandr, age=35), Person(name=Dmytro, age=36)]
