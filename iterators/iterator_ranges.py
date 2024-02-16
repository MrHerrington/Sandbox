def ranges(_numbers):
    """Функция преобразовывает числа из списка numbers в отрезки, представляя их в виде кортежей,
    где первый элемент кортежа является левой границей отрезка, второй элемент — правой границей
    отрезка. Полученные кортежи-отрезки функция возвращает в виде списка."""

    def ranges_iter():
        _iter = iter(_numbers)
        start_elem = next(_iter)
        next_elem = ''
        last_elem = ''
        try:
            while True:
                next_elem = next(_iter)
                if next_elem - start_elem == 1:
                    last_elem = next_elem
                    continue
                elif last_elem and next_elem - last_elem == 1:
                    last_elem = next_elem
                    continue
                else:
                    if not last_elem:
                        last_elem = start_elem
                    elif last_elem < start_elem:
                        last_elem = start_elem
                    yield start_elem, last_elem
                start_elem = next_elem
        except StopIteration:
            last_elem = next_elem
            yield start_elem, last_elem

    return list(ranges_iter())


numbers = [1, 2, 3, 4, 7, 8, 10]
print(ranges(numbers))

numbers = [1, 3, 5, 7]
print(ranges(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7]
print(ranges(numbers))
