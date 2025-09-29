def is_even(n: int) -> bool:
    """
    Check if a number is even.

    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
    >>> is_even(-4)
    True
    >>> is_even(-5)
    False
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Calculate factorial of a number.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    >>> factorial(-3)
    Traceback (most recent call last):
        ...
    ValueError: Factorial is not defined for negative numbers
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
