def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            return "нехватка аргуметов" if len(args) < 1 else "Слишком много аргументов"

        arg = args[0]
        if not isinstance(arg, int):
            return "Wrong types"
        if arg < 0:
            return "Negative argument"

        return func(*args, **kwargs)

    return wrapper


@validate_args
def my_function(n):
    return n * 2

