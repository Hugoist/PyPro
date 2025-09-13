import types
from typing import Type


def log_methods(cls: Type) -> Type:
    """ adds logs for method calls """
    for name, value in cls.__dict__.items():
        if isinstance(value, types.FunctionType):
            def wrapper(self, *args, __method=value, **kwargs):
                print(f"Logging: {__method.__name__} called with {args}{', ' + str(kwargs) if kwargs else ''}")
                return __method(self, *args, **kwargs)

            setattr(cls, name, wrapper)
    return cls


@log_methods
class MyClass:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


obj = MyClass()
obj.add(5, 3)  # Logging: add called with (5, 3)
obj.subtract(5, 3)  # Logging: subtract called with (5, 3)
