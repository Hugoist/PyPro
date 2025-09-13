import inspect
from typing import Type


def analyze_inheritance(cls: Type) -> None:
    """ shows parent of passed class"""
    print(f"Клас {cls.__name__} наслідує:")

    for base in cls.__mro__[1:]:
        if base is object:
            continue

        for name, func in base.__dict__.items():
            if inspect.isfunction(func):
                if name not in cls.__dict__:
                    print(f"- {name} з {base.__name__}")


class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


# Клас Child наслідує:
# - parent_method з Parent
analyze_inheritance(Child)
