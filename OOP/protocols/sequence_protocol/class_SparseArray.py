class SparseArray:
    def __init__(self, default_):
        if not isinstance(default_, list):
            self._sequence_ = [default_ for _ in range(100)]
        else:
            self._sequence_ = default_

    def __len__(self):
        return len(self._sequence_)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return SparseArray(self._sequence_[item])
        if not isinstance(item, int):
            raise TypeError('Индекс должен быть целым числом')
        if item < 0 or item >= len(self._sequence_):
            raise IndexError('Неверный индекс')
        return self._sequence_[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')
        if key < 0 or key >= len(self._sequence_):
            raise IndexError('Неверный индекс')
        self._sequence_[key] = value

    def __str__(self):
        return f'{self._sequence_}'

    def __repr__(self):
        return f'Sparse_Array({self._sequence_})'


# Test №1
array = SparseArray(0)

array[5] = 1000
array[12] = 1001

print(array[5])
print(array[12])
print(array[13])

# Test №2
array = SparseArray(None)

array[0] = 'Billy'
array[1] = 'Van'

print(array[0])
print(array[1])
print(array[2])
print(array[:10])
