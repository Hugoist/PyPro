from typing import Any, Dict, Type


class LoggingMeta(type):
    """Metaclass adds logging for attribute access and modification"""

    def __new__(cls: Type[type], name: str, bases: tuple[type, ...], namespace: Dict[str, Any]) -> type:
        cls = super().__new__(cls, name, bases, namespace)

        # Override __getattribute__ and __setattr__
        def __getattribute__(self, item: str) -> Any:
            value = super(cls, self).__getattribute__(item)
            print(f"Logging: accessed '{item}'")
            return value

        def __setattr__(self, key: str, value: Any) -> None:
            print(f"Logging: modified '{key}'")
            super(cls, self).__setattr__(key, value)

        cls.__getattribute__ = __getattribute__
        cls.__setattr__ = __setattr__

        return cls


class MyClass(metaclass=LoggingMeta):
    def __init__(self, name: str) -> None:
        self.name = name


obj = MyClass("Python") # Logging: modified 'name'

print(obj.name)
# Logging: accessed 'name'
# Python

obj.name = "New Python"  # Logging: modified 'name'
