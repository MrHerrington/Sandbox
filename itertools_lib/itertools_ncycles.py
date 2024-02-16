from itertools import chain, tee


def ncycles(_iterable, times):
    return chain.from_iterable(i for i in tee(_iterable, times))


print(*ncycles([1, 2, 3, 4], 3))

iterator = iter('bee')
print(*ncycles(iterator, 4))

iterator = iter([1])
print(*ncycles(iterator, 10))
