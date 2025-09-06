from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP


class Price:
    """Class representing a price with rounding to two decimals."""

    def __init__(self, amount: Decimal | float | str) -> None:
        # Always store as Decimal with 2 decimals
        self.amount = self._round_to_cents(Decimal(amount))

    def _round_to_cents(self, value: Decimal) -> Decimal:
        # round price to 2 digits after point

        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def __add__(self, other: Price) -> Price:
        # add prices

        return Price(self.amount + other.amount)

    def __sub__(self, other: Price) -> Price:
        # subtract prices

        return Price(self.amount - other.amount)

    def __eq__(self, other: Price) -> bool:
        # check if prices are equal

        return self.amount == other.amount

    def __lt__(self, other: Price) -> bool:
        # check if target price is lower than other

        return self.amount < other.amount

    def __gt__(self, other: Price) -> bool:
        # check if target price is higher than other

        return self.amount > other.amount

    def __repr__(self) -> str:
        # representing price in Price(amount) format

        return f"Price({self.amount})"


class PaymentGateway:
    """Class for managing user's financial transactions"""

    def __init__(self, initial_balance: Price) -> None:
        self.balance = initial_balance

    def charge(self, amount: Price) -> None:
        # charging balance

        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def deposit(self, amount: Price) -> None:
        # getting deposit

        self.balance += amount


p1 = Price(10.231)
p2 = Price(4.50)
p3 = Price(9.99)

print(f"{p1 = }")  # p1 = Price(10.23)
print(f"{p2 = }")  # p2 = Price(4.50)
print(f"{p3 = }")  # p3 = Price(9.99)

print(f"{p1 + p2 = }")  # p1 + p2 = Price(14.73)
print(f"{p1 - p2 = }")  # p1 - p2 = Price(5.73)

print(f"{p1 > p2 = }")  # p1 > p2 = True
print(f"{p1 < p3 = }")  # p1 < p3 = False
print(f"{p1 == Price(10.24) = }")  # p1 == Price(10.24) = False

print(f"{Price(7.777)}")  # Price(7.78)
print(f"{Price(7.774)}")  # Price(7.77)

initial_balance = Price(100.0)
gateway = PaymentGateway(initial_balance)

gateway.deposit(Price(50.0))
print("After deposit:", gateway.balance)  # After deposit: Price(150.00)

gateway.charge(Price(30.0))
print("After charge:", gateway.balance)  # After charge: Price(120.00)

try:
    gateway.charge(Price(200.0))  # Error: Insufficient funds
except ValueError as e:
    print("Error:", e)
