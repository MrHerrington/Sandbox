class Row:
    """Класс описывает объект, содержащий произвольный набор атрибутов"""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        if isinstance(self.__dict__[item], str):
            return self.__dict__[item].upper()
        else:
            return self.__dict__[item]

    def __setattr__(self, key, value):
        raise AttributeError('Установка нового атрибута невозможна')

    def __eq__(self, other):
        if isinstance(other, Row):
            return self._fields == other._fields
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self._fields)

    def __repr__(self):
        return 'Row(%s)' % ', '.join(f"{k}='{v}'" for k, v in self.__dict__.items())

    @property
    def _fields(self):
        return tuple(dict.fromkeys(self.__dict__))


# Test №1
row = Row(a='A', b='B', c='C')
print(row)
print(row.a, row.b, row.c)

# Test №2
row1 = Row(a=1, b=2, c=3)
row2 = Row(a=1, b=2, c=3)
row3 = Row(b=2, c=3, a=1)

print(row1 == row2)
print(hash(row1) == hash(row2))
print(row1 == row3)
print(hash(row1) == hash(row3))

# Test №3
row = Row(a=1, b=2, c=3)

try:
    row.d = 4
except AttributeError as e:
    print(e)
