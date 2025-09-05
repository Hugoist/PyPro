from typing import Iterable


def my_len(iterable: Iterable) -> int:
    """Return the length (the number of items) of an object."""

    count = 0
    for item in iterable:
        count += 1

    return count


def my_sum(iterable: Iterable[int]) -> int:
    """Return the sum of an iterable."""

    reult = 0
    for item in iterable:
        reult += item

    return reult


def my_min(iterable: Iterable[int]) -> int:
    """Return the minimum value of a iterable."""

    iterator = iter(iterable)
    try:
        minimum = next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

    for item in iterator:
        if item < minimum:
            minimum = item

    return minimum


numbers = [5, 2, 7, 1, 9]
empty_list = []

print(f"{my_len(numbers) = }")  # 5
print(f"{my_len(empty_list) = }")  # 0

print(f"{my_sum(numbers) = }")  # 24
print(f"{my_sum([]) = }")  # 0

print(f"{my_min(numbers) = }")  # 1

try:
    print(f"{my_min([]) = }")  # should raise ValueError
except ValueError as e:
    print("my_min([]) raised ValueError:", e)
