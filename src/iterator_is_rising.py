def is_rising(_iterable):
    _iter = iter(_iterable)
    temp = next(_iter)
    try:
        while True:
            current = next(_iter)
            if current <= temp:
                return False
            temp = current
    except StopIteration:
        return True


iterator = iter([1, 1, 1, 2, 3, 4])
print(is_rising(iterator))

iterator = iter(list(range(100, 200)))
print(is_rising(iterator))
