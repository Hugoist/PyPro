class DynamicProperties:
    """ Class allows to define dynamic properties """

    def add_property(self, name: str, default_value=None) -> None:
        private_name = f"_{name}"
        setattr(self, private_name, default_value)

        def getter(self):
            return getattr(self, private_name)

        def setter(self, value):
            setattr(self, private_name, value)

        prop = property(getter, setter)
        setattr(self.__class__, name, prop)


obj = DynamicProperties()
obj.add_property("name", "default_name")

print(obj.name)  # default_name
obj.name = "Python"
print(obj.name)  # Python
