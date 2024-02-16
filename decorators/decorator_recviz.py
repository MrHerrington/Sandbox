import functools


def recviz(func):
    """Декоратор полностью визуализирует выполнение декорируемой функции,
    в том числе и рекурсивной. Декоратор отображает все рекурсивные вызовы
    и возвращаемые значения, полученные при этих вызовах. Рекурсивные вызовы,
    выполняемые в глубину, отделяются друг от друга четырьмя пробелами."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        print(f"{wrapper.counter * '    '}-> {func.__name__}(" +
              ', '.join((*map(str, args), *(f'{k} = {v}' for k, v in kwargs.items()))) + ')')
        temp = func(*args, **kwargs)
        print(f"{wrapper.counter * '    '}<- {temp}")
        wrapper.counter -= 1
        return temp

    wrapper.counter = -1
    return wrapper


@recviz
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


fact(5)
