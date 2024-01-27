import functools


def prefix(symbol, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            if not to_the_end:
                return symbol + func(*args)
            else:
                return func(*args) + symbol
        return wrapper
    return decorator


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'


print(get_bonus())
