class AdvancedTuple(tuple):
    def __add__(self, other):
        return type(self)(list(self) + list(other))

    def __radd__(self, other):
        return type(self)(list(dict.fromkeys(other)) + list(self))

    def __iadd__(self, other):
        return type(self)(list(self) + list(other))


# Test №1
advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({'a': 1, 'b': 2} + advancedtuple)

# Test №2
advancedtuple = AdvancedTuple([1, 2, 3])

advancedtuple += [4, 5]
advancedtuple += iter([6, 7, 8])

print(advancedtuple)
print(type(advancedtuple))
