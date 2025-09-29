def calculate_discount(price: float, discount: float) -> float:
    """
    Calculate discount based on price and discount
    """
    if discount > 100:
        return 0
    return price * (1 - discount / 100)


# tests
print(calculate_discount(100, 20))  # 80.0
print(calculate_discount(50, 110))  # 0.0
