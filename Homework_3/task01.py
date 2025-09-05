from __future__ import annotations

import math


class Fraction:
    """Class for working with fractions"""

    def __init__(self, numerator: int, denominator: int) -> None:
        gcd: int = math.gcd(numerator, denominator)
        self.numerator: int = numerator // gcd
        self.denominator: int = denominator // gcd

    def __add__(self, other: Fraction) -> Fraction:
        # Add two fractions
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other: Fraction) -> Fraction:
        # Subtract two fractions
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other: Fraction) -> Fraction:
        # Multiply two fractions
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other: Fraction) -> Fraction:
        # Divide two fractions
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __repr__(self) -> str:
        # Display fraction in "numerator/denominator" format
        return f"{self.numerator}/{self.denominator}"


a = Fraction(1, 2)
b = Fraction(3, 4)

print(a + b)  # 5/4
print(a - b)  # -1/4
print(a * b)  # 3/8
print(a / b)  # 2/3
