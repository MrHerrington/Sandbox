import functools


def trace(func):
    """Выводит отладочную информацию о декорируемой функции во время ее выполнения,
    а именно: имя функции, переданные аргументы и возвращаемое значение"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}")
        print(f"TRACE: возвращаемое значение {func.__name__}(): {func(*args, **kwargs)}")
    return inner


@trace
def sub(a, b, c):
    """прекрасная функция"""
    return a - b + c


print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)
