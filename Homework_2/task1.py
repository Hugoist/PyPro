import builtins  # to access the original built-in sum


def my_sum() -> None:
    print("This is my custom sum function!")


numbers = [1, 2, 3, 4, 5]

# Using the original built-in sum
print("Вбудована сума:", builtins.sum(numbers))

# Calling our custom function
my_sum()

# Shadowing the built-in name 'sum'
sum = my_sum

# Now 'sum' calls our custom function
sum()

# Access built-in sum even after it was shadowed
print("Вбудована сума через builtins:", builtins.sum(numbers))
