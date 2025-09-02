# Global list of subscribers
subscribers: list[str] = []


def subscribe(name: str) -> None:
    """Add the subscriber's name to the global list"""

    subscribers.append(name)

    # Show confirm subscription message
    def confirm_subscription() -> None:
        print(f"Підписка підтверджена для {name}")

    # Call nested function and return its result
    return confirm_subscription()


def unsubscribe(name: str) -> None:
    """Check if the subscriber exists in the list and show unsubscribe confirmation message"""

    if name in subscribers:
        subscribers.remove(name)
        print(f"{name} успішно відписаний")
    else:
        print(f"Підписник {name} не знайдений")


subscribe("Олена")  # Підписка підтверджена для Olena
subscribe("Ігор")  # Підписка підтверджена для Ihor
print(subscribers)  # ['Олена', 'Ігор']
unsubscribe("Ігор")  # 'Ігор успішно відписаний'
unsubscribe("Олександр")  # 'Підписник Олександр не знайдений'
print(subscribers)  # ['Олена']
