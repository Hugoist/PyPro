class ProductWithGetSet:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def set_price(self, price: float) -> None:
        self.price = price


class ProductWithProperty:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        self._price = price


class PriceDescriptor:
    def __init__(self, default: float = 0.0) -> None:
        self._value = default

    def __get__(self, instance: object, owner: type | None) -> float:
        return self._value

    def __set__(self, instance: object, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._value = value


class ProductWithDescriptor:
    price: PriceDescriptor = PriceDescriptor()

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


# 1. getters/setters
p1 = ProductWithGetSet("Book", 20.0)
print("Initial price:", p1.get_price())  # Initial price: 20.0
p1.set_price(25.0)
print("Updated price:", p1.get_price())  # Updated price: 25.0
try:
    p1.set_price(-10.0)
except ValueError as e:
    print("Error:", e)  # Error: Price cannot be negative

# 2. @property
p2 = ProductWithProperty("Pen", 5.0)
print("Initial price:", p2.price)  # Initial price: 5.0
p2.price = 6.0
print("Updated price:", p2.price)  # Updated price: 6.0
try:
    p2.price = -2.0
except ValueError as e:
    print("Error:", e)  # Error: Price cannot be negative

# 3. descriptor
p3 = ProductWithDescriptor("Notebook", 15.0)
print("Initial price:", p3.price)  # Initial price: 15.0
p3.price = 18.0
print("Updated price:", p3.price)  # Updated price: 18.0
try:
    p3.price = -5.0
except ValueError as e:
    print("Error:", e)  # Error: Price cannot be negative
