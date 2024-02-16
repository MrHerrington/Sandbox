from itertools import tee


def grouper(_iterable, _count):
    """Функция возвращает итератор, генерирующий последовательность, элементами которой являются
    объединенные в кортежи по _count элементов соседние элементы итерируемого объекта _iterable.
    Если у элемента не достаточно соседей, то ими становится значение None."""
    _iter = iter(_iterable)
    while True:
        _iterator = (next(_iter, None) for _ in range(_count))
        a, b = tee(_iterator)
        counter = 0
        for i in b:
            if i is None:
                counter += 1
        if counter == _count:
            break
        else:
            yield tuple(a)


iterator = iter([1, 2, 3, 4, 5, 6, 7])
print(*grouper(iterator, 3))

numbers = [1, 2, 3, 4, 5, 6]
print(*grouper(numbers, 2))

iterator = iter([1, 2, 3])
print(*grouper(iterator, 5))
