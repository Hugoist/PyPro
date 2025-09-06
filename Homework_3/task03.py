from __future__ import annotations

from typing import List


class Person:
    """ Simple class for working with person"""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __lt__(self, other: Person) -> bool:
        # Compare if target person is older than other one

        return self.age < other.age

    def __gt__(self, other: Person) -> bool:
        # Compare if target person is younger than other one

        return self.age > other.age

    def __eq__(self, other: Person) -> bool:
        # Check of target person has same age as other one

        return self.age == other.age

    def __repr__(self) -> str:
        # Display person in Person(name, age) format

        return f"Person(name={self.name}, age={self.age})"


def sorted_persons(persons: List[Person]) -> List[Person]:
    """sort persons by age"""

    return sorted(persons)


p1 = Person("Oleksandr", 35)
p2 = Person("Dmytro", 36)
p3 = Person("Serhii", 34)

print(p1)  # Person(name=Oleksandr, age=35)
print(p2)  # Person(name=Dmytro, age=36)
print(p3)  # Person(name=Serhii, age=34)

print(sorted_persons(
    [p1, p2, p3]))  # [Person(name=Serhii, age=34), Person(name=Oleksandr, age=35), Person(name=Dmytro, age=36)]
