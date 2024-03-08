from collections.abc import Iterator, Iterable


def is_iterator(obj):
    return isinstance(obj, Iterator)


def is_iterable(obj):
    return isinstance(obj, Iterable)


# Test №1
print(is_iterable(123))
print(is_iterable([1, 2, 3]))
print(is_iterable((1, 2, 3)))
print(is_iterable('123'))
print(is_iterable(iter('123')))
print(is_iterable(map(int, '123')))

# Test №2
print(is_iterator(123))
print(is_iterator([1, 2, 3]))
print(is_iterator((1, 2, 3)))
print(is_iterator('123'))
print(is_iterator(iter('123')))
print(is_iterator(map(int, '123')))
