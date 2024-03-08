from collections import UserList


class SortedList(UserList):
    def __init__(self, *args):
        super().__init__(*args)
        self.data.sort()

    def __str__(self):
        return f'SortedList({self.data})'

    def add(self, obj):
        self.data.insert(-1, obj)
        self.data.sort()

    def discard(self, obj):
        while obj in self.data:
            self.data.remove(obj)
        self.data.sort()

    def update(self, iterable):
        self.data.extend(iterable)
        self.data.sort()


# Test №1
numbers = SortedList([5, 3, 4, 2, 1])

print(numbers)
print(numbers[1])
print(numbers[-2])
numbers.add(0)
print(numbers)
numbers.discard(4)
print(numbers)
numbers.update([4, 6])
print(numbers)

# Test №2
numbers = SortedList([5, 3, 4, 2, 1])

print(len(numbers))
print(*numbers)
print(1 in numbers)
print(6 in numbers)


# Test №3
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

print(numbers1 + numbers2)
print(numbers1 * 2)
print(numbers2 * 2)
