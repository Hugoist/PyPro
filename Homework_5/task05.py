class MutableClass:
    """class that allows adding and removing attributes dynamically"""

    def add_attribute(self, name: str, value):
        # adds new attribute
        setattr(self, name, value)

    def remove_attribute(self, name: str):
        # delete existing attribute
        if hasattr(self, name):
            delattr(self, name)
        else:
            raise AttributeError(f"No such attribute: {name}")


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")

#Attribute error: 'MutableClass' object has no attribute 'name'
try:
    print(obj.name)
except AttributeError as ae:
    print(f"Attribute error: {ae}")
