from __future__ import annotations

import math


class Vector:
    """Class for working with 3D vectors"""

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: Vector) -> Vector:
        # Add two vectors
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector) -> Vector:
        # Subtract two vectors
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> Vector:
        # Multiply vector by a scalar
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __lt__(self, other: Vector) -> bool:
        # Compare vectors by length
        return self.length() < other.length()

    def __gt__(self, other: Vector) -> bool:
        # Compare vectors by length
        return self.length() > other.length()

    def __eq__(self, other: Vector) -> bool:
        # Check equality with float precision
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y) and math.isclose(self.z, other.z)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"

    def length(self) -> float:
        # Magnitude of vector
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(1, 2, 3)

print("v1:", v1)  # v1: Vector(1, 2, 3)
print("v2:", v2)  # v2: Vector(4, 5, 6)
print("v1 + v2 =", v1 + v2)  # v1 + v2 = Vector(5, 7, 9)
print("v1 - v2 =", v1 - v2)  # v1 - v2 = Vector(-3, -3, -3)
print("v1 * 2 =", v1 * 2)  # v1 * 2 = Vector(2, 4, 6)
print("Length v1:", v1.length())  # Length v1: 3.7416573867739413
print("v1 < v2:", v1 < v2)  # v1 < v2: True
print("v1 > v2:", v1 > v2)  # v1 > v2: False
print("v1 == v2:", v1 == v2)  # v1 == v2: False
print("v1 == v3:", v1 == v3)  # v1 == v3: True
print("v1 == Vector(1,2,3):", v1 == Vector(1, 2, 3))  # v1 == Vector(1,2,3): True
