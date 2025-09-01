import math

def calculate_circle_area(radius: float) -> float:
    """Return the area of a circle by its radius"""
    return math.pi * radius ** 2


r = float(input("Enter radius: "))
print("Area:", calculate_circle_area(r))