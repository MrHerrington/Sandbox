class TakesNumbers:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        if all(isinstance(i, (int, float)) for i in args):
            return self.func(*args)
        else:
            raise TypeError('Аргументы должны принадлежать типам int или float')


# Test №1
@TakesNumbers
def mul(a, b):
    return a * b


print(mul(1, 2))
print(mul(1, 2.5))
print(mul(1.5, 2))
print(mul(1.5, 2.5))


# Test №2
@TakesNumbers
def mul(a, b):
    return a * b


try:
    print(mul(1, '2'))
except TypeError as error:
    print(error)
