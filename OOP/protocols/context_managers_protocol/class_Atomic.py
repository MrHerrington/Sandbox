from copy import copy, deepcopy


class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.copy = deepcopy(self.data) if deep else copy(self.data)

    def __enter__(self):
        return self.copy

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            return self.data
        else:
            self.data.clear()
            if isinstance(self.data, list):
                self.data.extend(self.copy)
            else:
                self.data.update(self.copy)
        return True


# Test №1
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[1]

print(numbers)

# Test №2
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[100]  # обращение по несуществующему индексу

print(numbers)

# Test №3
matrix = [[1, 2], [3, 4]]

with Atomic(matrix) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)

# Test №4
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)
