class SkipIterator:
    def __init__(self, iterable_, n):
        self.iterable_ = iterable_
        self.n = n
        self._index = -1
        self._iterator = ''

    def __iter__(self):
        self._iterator = range(self.iterable_[0], self.iterable_[-1] + 1, self.n + 1)
        yield from self._iterator

    def __next__(self):
        self._index += 1
        if self._index >= len(self._iterator):
            raise StopIteration
        return self._iterator[self._index]


# Test №1
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],1)
print(*skipiterator)

# Test №2
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)
print(*skipiterator)

# Test №3
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],0)
print(*skipiterator)
