class PermaDict:
    """Класс описывает словарь, который позволяет добавлять и удалять пары
    (<ключ>, <значение>), но не позволяет изменять значения по уже имеющимся ключам."""
    def __init__(self, sequence_=None):
        if sequence_ is None:
            self._sequence_ = dict()
        else:
            self._sequence_ = sequence_

    def __len__(self):
        return len(self._sequence_)

    def __iter__(self):
        yield from self._sequence_

    def __getitem__(self, item):
        if item in self._sequence_:
            return self._sequence_[item]
        return None

    def __setitem__(self, key, value):
        if key in self._sequence_:
            raise KeyError('Изменение значения по ключу невозможно')
        else:
            self._sequence_[key] = value

    def __delitem__(self, key):
        if key in self._sequence_:
            del self._sequence_[key]

    def __str__(self):
        return f'{self._sequence_}'

    def __repr__(self):
        return f'PermaDict({self._sequence_})'

    def keys(self):
        return self._sequence_.keys()

    def values(self):
        return self._sequence_.values()

    def items(self):
        return self._sequence_.items()


# Test №1
permadict = PermaDict({'name': 'Jerar', 'city': 'Moscow'})

print(permadict['name'])
print(len(permadict))

# Test №2
permadict = PermaDict({'name': 'Jerar', 'city': 'Moscow', 'age': 40})

print(*permadict)
print(*permadict.keys())
print(*permadict.values())
print(*permadict.items())

# Test №3
permadict = PermaDict()

permadict['name'] = 'Jerar'
permadict['age'] = 40
del permadict['name']
print(permadict['age'])
print(len(permadict))

# Test №4
permadict = PermaDict({'name': 'Jerar', 'city': 'Moscow'})

try:
    permadict['name'] = 'Arthur'
except KeyError as e:
    print(e)
