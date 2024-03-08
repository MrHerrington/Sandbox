from collections import UserList


class NumberList(UserList):
    def __new__(cls, iterable, *args, **kwargs):
        if all(map(lambda x: type(x) in (int, float), iterable)):
            return super().__new__(cls)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def __setitem__(self, key, value):
        if isinstance(value, int):
            if key in range(-len(self), len(self)):
                self.data[key] = value
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')


# Test №1
numberlist = NumberList([1, 2])

numberlist.append(3)
numberlist.extend([4, 5])
numberlist.insert(0, 0)

print(numberlist)

# Test №2
numberlist = NumberList([0, 1.0])

numberlist[1] = 1
numberlist = numberlist + NumberList([2, 3])
numberlist += NumberList([4, 5])

print(numberlist)

# Test №3
try:
    numberlist = NumberList(['a', 'b', 'c'])
except TypeError as error:
    print(error)
