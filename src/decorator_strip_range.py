import functools


def strip_range(start, end, char='.'):
    """Декоратор изменяет возвращаемое значение декорируемой функции, заменяя все символы в
    диапазоне индексов от start (включительно) до end (не включительно) на символ char. """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            datas = func(*args, **kwargs)
            new_datas = ''
            for i in range(len(datas)):
                if start <= i < end:
                    new_datas += char
                else:
                    new_datas += datas[i]
            return new_datas
        return wrapper
    return decorator


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'


print(beegeek())
