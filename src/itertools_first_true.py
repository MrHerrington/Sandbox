from itertools import dropwhile


def first_true(_iter, _func):
    return next(dropwhile(lambda x: not (_func(x)), _iter))


numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])
print(first_true(numbers, lambda num: num > 10))
