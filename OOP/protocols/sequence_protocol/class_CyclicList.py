from itertools import cycle


class CyclicList:
    def __init__(self, sequence_):
        self._sequence_ = sequence_

    def __len__(self):
        return len(self._sequence_)

    def __iter__(self):
        yield from cycle(self._sequence_)

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Индекс должен быть целым числом')
        if item < 0:
            raise IndexError('Неверный индекс')
        while item >= len(self._sequence_):
            item -= len(self._sequence_)
        return self._sequence_[item]

    def __str__(self):
        return f'{self._sequence_}'

    def __repr__(self):
        return f'Sparse_Array({self._sequence_})'

    def append(self, item):
        return self._sequence_.append(item)

    def pop(self, index=-1):
        return self._sequence_.pop(index)


# Test №1
cyclic_list = CyclicList([1, 2, 3])

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')
print()


# Test №2
cyclic_list = CyclicList([1, 2, 3])

cyclic_list.append(4)
print(cyclic_list.pop())
print(len(cyclic_list))
print(cyclic_list.pop(0))
print(len(cyclic_list))
