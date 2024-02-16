def starmap(func, iterable):
    """Функция работает аналогично функции map(), но принимает не один аргумент —
    коллекцию (элемент iterable), а каждый элемент этой коллекции в качестве
    самостоятельного аргумента."""
    for i in iterable:
        yield func(*i)


pairs = [(1, 3), (2, 5), (6, 4)]
print(*starmap(lambda a, b: a + b, pairs))


points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]
print(*starmap(lambda x, y, z: x * y * z, points))
