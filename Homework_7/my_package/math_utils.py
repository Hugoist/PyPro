def factorial(n: int) -> int:
    """
    Calculate factorial
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n in (0, 1) else n * factorial(n - 1)


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a
