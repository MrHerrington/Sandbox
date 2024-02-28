class ReversedSequence:
    def __init__(self, sequence_):
        self._sequence_ = sequence_

    def __len__(self):
        return len(self._sequence_)

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Индекс должен быть целым числом')
        if item < 0 or item >= len(self._sequence_):
            raise IndexError('Неверный индекс')
        return self._sequence_[len(self) - item - 1]

    def __str__(self):
        return f'{self._sequence_}'

    def __repr__(self):
        return f'ReversedSequence({self._sequence_})'


# Test №1
reversed_list = ReversedSequence([1, 2, 3, 4, 5])

print(reversed_list[0])
print(reversed_list[1])
print(reversed_list[2])

# Test №2
numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)

print(reversed_numbers[0])
numbers.append(6)
print(reversed_numbers[0])


# Test №3
numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)
print(len(reversed_numbers))

numbers.append(6)
numbers.append(7)
print(len(reversed_numbers))
