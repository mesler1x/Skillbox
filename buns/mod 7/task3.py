import time
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"

        arg = args[0]
        if not isinstance(arg, int):
            return "Wrong types"
        if arg < 0:
            return "Negative argument"

        return func(*args, **kwargs)

    return wrapper


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


class Timer:
    def __init__(self):
        self.active = False

    def __call__(self, func):
        def wrapper(*args):
            if self.active:
                return func(*args)
            start = time.time()
            self.active = True
            res = func(*args)
            end = time.time()
            self.active = False
            return res, end - start

        return wrapper


