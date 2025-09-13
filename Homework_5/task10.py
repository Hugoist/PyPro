from typing import Any


class SingletonMeta(type):
    """ Ensures that a class can only have one instance """
    _instances: dict[type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """Example class that uses SingletonMeta metaclass"""

    def __init__(self) -> None:
        print("Creating instance")


obj1 = Singleton()  # "Creating instance"
obj2 = Singleton()
print(obj1 is obj2)  # True
