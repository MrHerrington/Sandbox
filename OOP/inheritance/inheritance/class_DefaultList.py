from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable, default=None):
        super().__init__(iterable)
        self.default = default

    def __getitem__(self, item):
        if item not in range(-len(self), len(self)):
            return self.default
        else:
            return self.data[item]


# Test №1
defaultlist = DefaultList([1, 2, 3])
print(defaultlist[0])
print(defaultlist[-1])
print(defaultlist[100])
print(defaultlist[-100])

# Test №2
defaultlist = DefaultList([1, 2, 3], 0)
print(defaultlist[0])
print(defaultlist[-1])
print(defaultlist[100])
print(defaultlist[-100])
