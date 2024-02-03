def around(_iterable):
    _iterator = iter(_iterable)
    start = None
    current = next(_iterator)
    last = next(_iterator)
    try:
        while True:
            yield start, current, last
            start = current
            current = last
            last = next(_iterator)
    except StopIteration:
        last = None
        yield start, current, last


numbers = [1, 2, 3, 4, 5]
print(*around(numbers))

iterator = iter('hey')
print(*around(iterator))
