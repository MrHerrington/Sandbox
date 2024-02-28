class OrderedSet:
    """Класс описывает упорядоченное множество"""
    def __init__(self, sequence_=None):
        if sequence_ is None:
            self._sequence_ = list()
        else:
            self._sequence_ = list(dict.fromkeys(sequence_))

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

    def add(self, item):
        if item not in self._sequence_:
            self._sequence_.append(item)

    def discard(self, item):
        if item in self._sequence_:
            self._sequence_.remove(item)


# Test №1
orderedset = OrderedSet(['van', 'python', 'stepik', 'van', 'dungeon', 'python', 'van'])

print(*orderedset)
print(len(orderedset))

# Test №2
orderedset = OrderedSet(['van', 'python', 'stepik', 'van', 'dungeon', 'python', 'van'])

print('python' in orderedset)
print('C++' in orderedset)

# Test №3
orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)
