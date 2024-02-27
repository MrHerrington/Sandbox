class Peekable:
    def __init__(self, iterable_):
        self._iterable_ = iterable_
        self._index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self._iterable_):
            raise StopIteration
        return self._iterable_[self._index]

    def peek(self, default=''):
        if self._index + 1 >= len(self._iterable_):
            if default == '':
                raise StopIteration
            else:
                return default
        return self._iterable_[self._index + 1]


# Test №1
iterator = Peekable('dungeon')

print(next(iterator))
print(next(iterator))
print(*iterator)

# Test №2
iterator = Peekable('Python')

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())

# Test №3
iterator = Peekable('Python')

print(*iterator)
print(iterator.peek(None))
