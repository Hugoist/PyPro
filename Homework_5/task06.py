class Proxy:
    """ define class for logging method calls"""

    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, name):
        attr = getattr(self.obj, name)

        if callable(attr):
            def wrapper(*args, **kwargs):
                log_msg = f"\nCalling method\n{name}"

                if args:
                    log_msg += f" with args: {args}"

                if kwargs:
                    if args:
                        log_msg += f" and"

                    log_msg += f" with kwargs: {kwargs}"

                print(log_msg)
                return attr(*args, **kwargs)

            return wrapper
        else:
            return attr


class MyClass:
    def greet(self, name: str, adj: str = ""):
        return f"Hello, {adj} {name}!"


obj = MyClass()
proxy = Proxy(obj)

# Calling method
# greet with args: ('Alice',)
# Hello,  Alice!
print(proxy.greet("Alice"))

# Calling method
# greet with args: ('Alice',) and with kwargs: {'adj': 'dear'}
# Hello, dear Alice!
print(proxy.greet("Alice", adj="dear"))
