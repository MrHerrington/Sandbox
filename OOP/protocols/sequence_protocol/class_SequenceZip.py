class SequenceZip:
    def __init__(self, *args):
        self._sequence_ = list(zip(*args))

    def __len__(self):
        return len(self._sequence_)

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Индекс должен быть целым числом')
        if item < 0:
            raise IndexError('Неверный индекс')
        while item >= len(self._sequence_):
            item -= len(self._sequence_)
        return self._sequence_[item]

    def __iter__(self):
        yield from self._sequence_

    def __str__(self):
        return f'{self._sequence_}'

    def __repr__(self):
        return f'Sparse_Array({self._sequence_})'


# Test №1
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(list(sequencezip))
print(tuple(sequencezip))

# Test №2
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])
print(len(sequencezip))
print(sequencezip[1])
print(sequencezip[2])
