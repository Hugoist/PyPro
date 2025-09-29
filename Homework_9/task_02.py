from typing import List, Tuple


def filter_adults(people: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Returns list of people older than 18 years
    """
    return list(filter(lambda p: p[1] >= 18, people))


# tests
people = [("Андрій", 25), ("Олег", 16), ("Марія", 19), ("Ірина", 15)]
print(filter_adults(people))
# [("Андрій", 25), ("Марія", 19)]
