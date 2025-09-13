from typing import Any, Dict, Type


class LimitedAttributesMeta(type):
    """Metaclass that restricts the maximum number of attributes in a class."""

    MAX_ATTRIBUTES: int = 3  # maximum allowed attributes

    def __new__(cls: Type[type], name: str, bases: tuple[type, ...], namespace: Dict[str, Any]) -> type:
        # filter system attributes
        user_attrs = {k: v for k, v in namespace.items() if not k.startswith("__")}

        if len(user_attrs) > cls.MAX_ATTRIBUTES:
            raise TypeError(
                f"Class {name} cannot have more than {cls.MAX_ATTRIBUTES} attributes."
            )

        return super().__new__(cls, name, bases, namespace)


class LimitedClass(metaclass=LimitedAttributesMeta):
    attr1 = 1
    attr2 = 2
    attr3 = 3


try:
    # TypeError: Class LimitedClass2 cannot have more than 3 attributes.
    class LimitedClass2(metaclass=LimitedAttributesMeta):
        attr1 = 1
        attr2 = 2
        attr3 = 3
        attr4 = 4
except TypeError as te:
    print(f"TypeError: {te}")
