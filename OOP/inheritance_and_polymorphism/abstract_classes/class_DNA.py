from collections.abc import Sequence


class DNA(Sequence):
    __BASE = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}

    def __init__(self, chain):
        self._chain = chain

    def __str__(self):
        return self._chain

    def __len__(self):
        return len(self._chain)

    def __getitem__(self, index):
        if isinstance(index, (int, slice)):
            return self._chain[index], type(self).__BASE[self._chain[index]]
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._chain == other._chain
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._chain + other._chain)
        return NotImplemented

    def __contains__(self, item):
        return item in self._chain


# Test №1
dna = DNA('AGTC')

print(dna[0])
print(dna[1])
print(dna[2])
print(dna[3])
print(dna[-1])
print(dna[-2])

# Test №2
dna = DNA('AGT')

print(dna)
print(len(dna))
print('A' in dna)
print('C' in dna)

# Test №3
dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')

dna3 = dna1 + dna2
dna4 = dna2 + dna1

print(dna3, type(dna3))
print(dna4, type(dna4))

# Test №4
dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')
dna3 = DNA('TTTAAT')

print(dna1 == dna2)
print(dna2 == dna3)
print(dna1 != dna3)
print(dna2 != dna3)
