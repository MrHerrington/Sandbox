class LoopTracker:
    def __init__(self, iterable_):
        self._iterable_ = iterable_
        self._index = -1
        self._empty_accesses = 0
        self._first = None
        self._last = None

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self._iterable_):
            self._empty_accesses += 1
            raise StopIteration
        if self._first is None:
            self._first = self._iterable_[self._index]
        self._last = self._iterable_[self._index]
        return self._iterable_[self._index]

    @property
    def accesses(self):
        return self._index + 1

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if self._first:
            return self._first
        if self._index + 1 >= len(self._iterable_):
            self._empty_accesses += 1
            raise AttributeError('Исходный итерируемый объект пуст')
        if self._first is None:
            self._first = self._iterable_[self._index + 1]
        return self._first


    @property
    def last(self):
        if self._last is None:
            raise AttributeError('Последнего элемента нет')
        return self._last

    def is_empty(self):
        if self._index + 1 < len(self._iterable_):
            return False
        else:
            return True


# TEST_1:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(list(loop_tracker))

# TEST_2:
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.accesses)
next(loop_tracker)
next(loop_tracker)
print(loop_tracker.accesses)

# TEST_3:
loop_tracker = LoopTracker([1, 2, 3])
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

# TEST_4:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

# TEST_5:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.empty_accesses)
next(loop_tracker)
next(loop_tracker)

for _ in range(5):
    try:
        next(loop_tracker)
    except StopIteration:
        pass

print(loop_tracker.empty_accesses)

# TEST_6:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())

# TEST_7:
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.first)
print(next(loop_tracker))

# TEST_8:
loop_tracker = LoopTracker([])

try:
    print(loop_tracker.first)
except AttributeError as e:
    print(e)

# TEST_9:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)
print(next(loop_tracker))
print(loop_tracker.last)

# TEST_10:
loop_tracker = LoopTracker([1, 2, 3])

try:
    print(loop_tracker.last)
except AttributeError as e:
    print(e)
