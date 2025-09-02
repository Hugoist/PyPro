from typing import Callable, Any


def create_calculator(operator: str) -> Callable[[float, float], Any]:
    """Create functions for basic calculations"""

    # Dictionary mapping operators to corresponding lambda functions
    operations: dict[str, Callable[[float, float], float]] = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else float('inf')  # Return inf for division by zero
    }

    if operator in operations:
        return operations[operator]
    else:
        return lambda x, y: f"Невідомий оператор '{operator}'"


add_calc = create_calculator('+')
sub_calc = create_calculator('-')
mul_calc = create_calculator('*')
div_calc = create_calculator('/')
exp_calc = create_calculator('**')

print(add_calc(5, 3))  # 8
print(sub_calc(5, 3))  # 2
print(mul_calc(5, 3))  # 15
print(div_calc(5, 2))  # 2.5
print(div_calc(5, 0))  # inf
print(exp_calc(5, 2))  # Невідомий оператор '**'
