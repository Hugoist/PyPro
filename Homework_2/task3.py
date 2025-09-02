discount = 0.1  # (10% discount)


def create_order(price: float, extra_discount: float = 0) -> None:
    """Create order with applied discounts"""

    price_with_discount: float = price * (1 - discount)

    # Apply additional discount to the discounted price
    def apply_additional_discount() -> None:
        nonlocal price_with_discount

        price_with_discount *= (1 - extra_discount)

    apply_additional_discount()

    def get_total_discount_in_percents() -> float:
        return (discount + extra_discount) * 100

    # Print the final calculated price
    print(
        f"Початкова ціна: {price:.0f}, кінцева ціна зі знижкою {get_total_discount_in_percents():.0f}%: {price_with_discount:.0f}")


create_order(1000)  # Початкова ціна: 1000, кінцева ціна зі знижкою 10%: 900
