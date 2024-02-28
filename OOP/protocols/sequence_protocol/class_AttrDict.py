class AttrDict:
    """Класс описывает упрощенный словарь"""
    def __init__(self, sequence_=None):
        if sequence_ is None:
            self._sequence_ = dict()
        else:
            self._sequence_ = sequence_
        self.__dict__.update(**self._sequence_)

    def __len__(self):
        return len(self._sequence_)

    def __getattr__(self, item):
        return self.__dict__[item]

    def __getitem__(self, item):
        if item in self._sequence_:
            return self._sequence_[item]
        return None

    def __setitem__(self, key, value):
        self._sequence_[key] = value
        self.__dict__.update(**self._sequence_)

    def __str__(self):
        return f'{self._sequence_}'

    def __repr__(self):
        return f'AttrDict({self._sequence_})'


# Test №1
attrdict = AttrDict({'name': 'X Æ A-12', 'father': 'Elon Musk'})
print(attrdict['name'])
print(attrdict.father)
print(len(attrdict))

# Test №2
attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})

attrdict['city'] = 'Dubai'
attrdict['age'] = 31
print(attrdict.city)
print(attrdict.age)

# Test №3
attrdict = AttrDict()
attrdict['school_name'] = 'DUNGEON'
print(attrdict['school_name'])
print(attrdict.school_name)
