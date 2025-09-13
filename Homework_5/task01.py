def analyze_object(target_obj: object) -> None:
    """get type and attributes/methods  from an object"""

    print(f"Tип об'єкта: {type(target_obj)}")

    print("Атрибути і методи:")

    for attr in dir(target_obj):
        # skip system attributes
        if attr.startswith("__"):
            continue

        # try:
        attr_value = getattr(target_obj, attr)
        print(f"\t- {attr}: {type(attr_value)}")
        # except AttributeError:


class MyClass:
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


obj = MyClass("World")

analyze_object(obj)
# Tип об'єкта: <class '__main__.MyClass'>
# Атрибути і методи:
# - say_hello: <class 'method'>
# - value: <class 'str'>
