import importlib
import inspect


def analyze_module(module_name: str) -> None:
    """get functions and classes from a module"""

    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Модуль '{module_name}' не знайдено")
        return

    # get functions
    functions = inspect.getmembers(module, inspect.isbuiltin)
    # get classes
    classes = inspect.getmembers(module, lambda cls: inspect.isclass(cls) and cls.__module__ == module_name)

    print("Функції:")
    if not functions:
        print(f"\t- <немає функцій у модулі {module.__name__}>")
    else:
        for name, func in functions:
            try:
                sig = str(inspect.signature(func)).replace(", /", "")
                print(f"\t- {name}{sig}")
            except ValueError:
                # if there are no signature
                print(f"\t- {name}(...)")

    print("\nКласи:")
    if not classes:
        print(f"\t- <немає класів у модулі {module.__name__}>")
    else:
        for name in classes:
            print(f"\t- {name}")


# Функції:
#     - acos(x)
#     - acosh(x)
#     ...
#     - hypot(...)
#     ...
#
# Класи:
#     - <немає класів у модулі math>
analyze_module("math")

