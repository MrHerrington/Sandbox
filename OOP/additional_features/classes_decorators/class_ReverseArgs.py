import functools


class ReverseArgs:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        functools.update_wrapper(self, self.func)
        return self.func(*reversed(args))


# Test №1
@ReverseArgs
def power(a, n):
    """docstring"""
    return a ** n


print(power(2, 3))
print(power.__doc__)


# Test №2
@ReverseArgs
def concat(a, b, c):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))
