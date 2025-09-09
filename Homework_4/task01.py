def calculator() -> None:
    print("Simple console calculator. Available operations: +, -, *, /. Type 'exit' to quit.")

    while True:
        try:
            expression = input("\nEnter expression (e.g. 5 + 2): ").strip()

            if expression == "exit":
                break

            # parse user's input
            parts = expression.split(" ")
            if len(parts) != 3:
                raise ValueError("Invalid expression. Use: number operator number")

            operand1, operator, operand2 = parts

            # convert operands to float
            operand1 = float(operand1)
            operand2 = float(operand2)

            # do calculations
            if operator == "+":
                result = operand1 + operand2
            elif operator == "-":
                result = operand1 - operand2
            elif operator == "*":
                result = operand1 * operand2
            elif operator == "/":
                if operand2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = operand1 / operand2
            else:
                raise UnknownOperationError(f"{operator}")

            print(result)

        except ZeroDivisionError as zde:
            print("Error:", zde)
        except ValueError as ve:
            print("Error:", ve)
        except UnknownOperationError as uoe:
            print("Error:", uoe)


class UnknownOperationError(Exception):
    """Raised when an unknown operation is requested."""

    def __init__(self, operator: str) -> None:
        self.operator = operator
        super().__init__(f"Operation \"{operator}\" is not available.")


calculator()
# Enter expression (e.g. 5 + 2): 5 % 3
# Error: Operation "%" is not available.

# Enter expression (e.g. 5 + 2): 5 + 1
# 6.0

# Enter expression (e.g. 5 + 2): 6 - 1
# 5.0

# Enter expression (e.g. 5 + 2): 2 * 2
# 4.0

# Enter expression (e.g. 5 + 2): 3 / 2
# 1.5

# Enter expression (e.g. 5 + 2): 5-1
# Error: Invalid expression. Use: number operator number

# Enter expression (e.g. 5 + 2): 5 / 0
# Error: Cannot divide by zero

# Enter expression (e.g. 5 + 2): exit
