import functools


class MaxCallsException(BaseException):
    pass


class LimitedCalls:
    calls = 0

    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if type(self).calls + 1 <= self.n:
                type(self).calls += 1
                return func(*args, **kwargs)
            else:
                raise MaxCallsException('Превышено допустимое количество вызовов')
        return wrapper


@LimitedCalls(3)
def add(a, b):
    """docstring"""
    return a + b


print(add(1, 2))
print(add(3, 4))
print(add(5, 6))
print(add.__doc__)

try:
    print(add())
except MaxCallsException as e:
    print(e)
