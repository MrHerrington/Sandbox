import builtins


def print_decorator(func: builtins) -> builtins:
    def wrapper(*args: object, **kwargs: str) -> None:
        builtins.print(*map(lambda x: x.upper(), args), **{k: v.upper() for k, v in kwargs.items()})
    return wrapper


@print_decorator
def print(*args: object, **kwargs: str) -> object:
    return *args, *kwargs


print('hi', 'there', sep='///', end='!!')
