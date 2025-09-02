from typing import Callable


def create_product(name: str, price: float, quantity: int) -> Callable[[float], None]:
    """Return function to update the price of the product using closure"""

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    print(f"Створений товар '{product['name']}' з ціною {price:.2f} та в кількості {quantity}")

    def update_price(new_price: float) -> None:
        """Update the product's price and print the change."""

        product["price"] = new_price
        print(f"Ціна товару '{product['name']}' оновлена на {new_price:.2f}")

    return update_price


apple_price_updater = create_product("Яблуко", 20.0, 100)  # Створений товар 'Яблуко' з ціною 20.00 та в кількості 100

apple_price_updater(25.0)  # Ціна товару 'Яблуко' оновлена на 25.00
apple_price_updater(30.5)  # Ціна товару 'Яблуко' оновлена на 30.50
