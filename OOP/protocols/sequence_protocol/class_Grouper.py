class Grouper:
    """Класс описывает объект, который группирует элементы некоторого
    итерируемого объекта на основе ключевой функции."""
    def __init__(self, iterable, key):
        self._iterable = iterable
        self._key = key
        self._dct = dict.fromkeys(map(self._key, self._iterable), None)
        for i in self._iterable:
            for k, v in self._dct.items():
                if self._key(i) == k:
                    if self._dct[k] is None:
                        self._dct[k] = [i]
                    else:
                        self._dct[k].append(i)

    def __len__(self):
        return len(self._dct)

    def __iter__(self):
        yield from self._dct

    def __getitem__(self, key):
        if key in self._dct:
            return self._dct[key]

    def add(self, item):
        if self._key(item) in self._dct:
            self._dct[self._key(item)].append(item)
        else:
            self._dct[self._key(item)] = [item]

    def group_for(self, item):
        return self._key(item)


# Test №1
grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

print(grouper[2])
print(grouper[3])
print(grouper[4])

# Test №2
grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

print(3 in grouper)
print('bee' in grouper)

# Test №3
grouper = Grouper(['hi'], key=lambda s: s[0])

print(len(grouper))

grouper.add('hello')
grouper.add('bee')
grouper.add('big')

print(len(grouper))

grouper.add('geek')

print(grouper['h'])
print(grouper['b'])
print(grouper['g'])
print(len(grouper))

# Test №4
grouper = Grouper(['hi'], key=lambda s: s[0])

print(grouper.group_for('hello'))
print(grouper.group_for('bee'))
print(grouper['h'])
print('b' in grouper)
