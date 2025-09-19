from math_utils import factorial, gcd
from string_utils import to_uppercase, trim_spaces

# Math utils
print("Factorial of 5:", factorial(5))  # Factorial of 5: 120
print("GCD of 36 and 60:", gcd(6, 9))  # GCD of 36 and 60: 12

# String utils
text = "   hello world   "
print("Uppercase:", to_uppercase(text))  # Uppercase:    HELLO WORLD
print("Trimmed:", trim_spaces(text))  # Trimmed: hello world
