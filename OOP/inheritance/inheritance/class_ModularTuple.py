class ModularTuple(tuple):
    def __new__(cls, iterable, size=100):
        return super().__new__(cls, tuple(map(lambda x: x % size, iterable)))


# Test №1
modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))

# Test №2

modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)

print(modulartuple)
