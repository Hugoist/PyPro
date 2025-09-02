total_expense: float = 0


def add_expense(expense: float) -> None:
    """Add an expense to the global total_expense."""

    global total_expense
    total_expense += expense


def get_expense() -> float:
    """Return the current total expense."""

    return total_expense


def expense_tracker() -> None:
    """Console interface for adding and viewing expenses."""

    while True:
        print("\nМеню трекера витрат:")
        print("1. Додати витрату")
        print("2. Показати загальну суму витрат")
        print("3. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            try:
                amount = float(input("Введіть суму витрати: "))
                add_expense(amount)
            except ValueError:
                print("Будь ласка, введіть коректне число.")
        elif choice == "2":
            print(f"Загальна сума витрат: {get_expense():.2f}")
        elif choice == "3":
            print("Вихід із трекера витрат.")
            break
        else:
            print("Невідома опція. Спробуйте ще раз.")


expense_tracker()
