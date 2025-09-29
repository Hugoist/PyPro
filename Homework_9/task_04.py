from typing import List, Union, TypeVar

T = TypeVar('T')

def get_first(data: List[T]) -> Union[T, None]:
    """
    Returns first element of list or None if list is empty
    """
    return data[0] if len(data) else None


# tests
print(get_first([1, 2, 3]))  # 1
print(get_first(["a", "b", "c"]))  # "a"
print(get_first([]))  # None
