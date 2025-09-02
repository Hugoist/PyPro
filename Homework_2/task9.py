from typing import Callable, Any


def memoize(func: Callable[[int], Any]) -> Callable[[Any], Any]:
    """Return a function that caches results of `func`"""

    cache: dict[int, Any] = {}  # dictionary to store cached results

    def wrapper(param: Any) -> Any:
        if param in cache:
            print(f"Отримано з кешу для {param}")
            return cache[param]
        result = func(param)
        cache[param] = result
        print(f"Обчислено та додано в кеш для {param}")
        return result

    return wrapper


def fibonacci(nmbr: int) -> int:
    """Return the nth Fibonacci number"""
    
    if nmbr <= 1:
        return nmbr
    return fibonacci(nmbr - 1) + fibonacci(nmbr - 2)


cached_fibonacci = memoize(fibonacci)

cached_fibonacci(1)
cached_fibonacci(2)
cached_fibonacci(3)
cached_fibonacci(2)
