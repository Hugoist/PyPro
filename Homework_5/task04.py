from typing import Callable


def create_class(class_name: str, methods: dict[str, Callable]):
    """create a class with defined methods"""
    return type(class_name, (object,), methods)


def say_hello(self):
    return "Hello!"


def say_goodbye(self):
    return "Goodbye!"


methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}

MyDynamicClass = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()
print(obj.say_hello())  # Hello!
print(obj.say_goodbye())  # Goodbye!
