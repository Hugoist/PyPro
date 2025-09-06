from __future__ import annotations

import math
from typing import List


class Vector:
    """ Class representing n-dimension vector """

    def __init__(self, coords: List[float | int]) -> None:
        self.coords = coords

    def __add__(self, other: Vector) -> Vector:
        # Add two vectors

        self.compare(other)
        return Vector([a + b for a, b in zip(self.coords, other.coords)])

    def __sub__(self, other: Vector) -> Vector:
        # Subtract two vectors

        self.compare(other)
        return Vector([a - b for a, b in zip(self.coords, other.coords)])

    def __mul__(self, other) -> Vector | float:
        # Multiply vector by a scalar or other Vector

        if isinstance(other, (int, float)):
            return Vector([a * other for a in self.coords])
        elif isinstance(other, Vector):
            self.compare(other)
            return sum(a * b for a, b in zip(self.coords, other.coords))
        else:
            raise TypeError(f"Unsupported operand type for *: 'Vector' and '{type(other).__name__}'")

    def __rmul__(self, other) -> Vector:
        # Multiply vector by a scalar or other Vector

        return self.__mul__(other)

    def __gt__(self, other: Vector) -> bool:
        # Compare vectors by length

        return self.length() > other.length()

    def __lt__(self, other: Vector) -> bool:
        # Compare vectors by length

        return self.length() < other.length()

    def __repr__(self) -> str:
        return f"Vector({self.coords})"

    def compare(self, other: Vector) -> None:
        # Compare Vectors by dimensions amount

        if not isinstance(other, Vector):
            raise TypeError("Vector expected")

        if len(self.coords) != len(other.coords):
            raise ValueError("Vectors must have same dimensions")

    def length(self) -> float:
        # Get magnitude of vector

        return math.sqrt(sum(a ** 2 for a in self.coords))


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([1, 2])

print(f"{v1}")  # Vector([1, 2, 3])
print(f"{v2}")  # Vector([4, 5, 6])
print(f"{v3}")  # Vector([1, 2])

print(f"{v1 + v2}")  # Vector([5, 7, 9])
print(f"{v2 - v1}")  # Vector([3, 3, 3])

print(f"{v1 * 2}")  # Vector([2, 4, 6])
print(f"{2 * v1}")  # Vector([2, 4, 6])
print(f"{v1 * v2}")  # 32

print(f"{v1.length()}")  # 3.7416573867739413
print(f"{v1 > v2}")  # False
print(f"{v1 < v2}")  # True

try:
    print(f"{v1 + v3}")  # ValueError: Vectors must have same dimensions
except ValueError as e:
    print("ValueError:", e)

try:
    print(v1 * "abc")  # TypeError: Unsupported operand type for *: 'Vector' and 'str'
except TypeError as e:
    print("TypeError:", e)
