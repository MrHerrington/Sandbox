from itertools import islice, count


def first_largest(_iter, _num):
    """Функция возвращает индекс первого элемента итерируемого объекта iterable,
    который больше number. Если таких элементов нет, функция возвращает число -1."""
    def _check():
        for _index, _nums in zip(count(), islice(_iter, None)):
            if _nums > _num:
                return _index
    check = _check()
    if check is None:
        return -1
    else:
        return check


iterator = iter([-1, -2, -3, -4, -5])
print(first_largest(iterator, 10))

numbers = [10, 2, 14, 7, 7, 18, 20]
print(first_largest(numbers, 11))
