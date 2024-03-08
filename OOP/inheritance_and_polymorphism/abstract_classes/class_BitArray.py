from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, array):
        self.array = array

    def __getitem__(self, index):
        if index in range(-len(self), len(self)):
            return self.array[index]

    def __len__(self):
        return len(self.array)

    def __invert__(self):
        return type(self)(map(lambda x: int(not x), self.array))

    def __str__(self):
        return f'{repr(list(self.array))}'

    def __or__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self_item | other_item for self_item, other_item in zip(self.array, other.array))
        return NotImplemented

    def __and__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self_item & other_item for self_item, other_item in zip(self.array, other.array))
        return NotImplemented


# Test №1
bitarray = BitArray([1, 0, 1, 1])

print(bitarray)
print(~bitarray)
print(bitarray[0])
print(bitarray[1])
print(bitarray[-1])
print(0 in bitarray)
print(1 not in bitarray)

# Test №2
bitarray1 = BitArray([1, 0, 1, 1])
bitarray2 = BitArray([0, 0, 0, 1])

bitarray3 = bitarray1 | bitarray2
bitarray4 = bitarray1 & bitarray2
bitarray5 = ~bitarray1

print(bitarray3, type(bitarray3))
print(bitarray4, type(bitarray4))
print(bitarray5, type(bitarray5))
