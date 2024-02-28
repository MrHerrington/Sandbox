class MutableString:
    """Класс описывает изменяемую строку"""
    def __init__(self, string):
        self._string = string

    def __len__(self):
        return len(self._string)

    def __iter__(self):
        yield from self._string

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self._string + other._string)
        else:
            return NotImplemented

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise ValueError('Некорректный тип данных!')
        if key >= len(self._string) or key < -len(self._string):
            raise IndexError('Некорректный индекс!')
        return self._string[key]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise ValueError('Некорректный тип данных!')
        if key >= len(self._string) or key < -len(self._string):
            raise IndexError('Некорректный индекс!')
        self._string = self._string.replace(self._string[key], value)

    def __str__(self):
        return f'{self._string}'

    def __repr__(self):
        return f"MutableString('{self._string}')"

    def lower(self):
        self._string = self._string.lower()

    def upper(self):
        self._string = self._string.upper()


# Test №1
mutablestring = MutableString('dungeon')

print(*mutablestring)
print(str(mutablestring))
print(repr(mutablestring))

# Test №2
mutablestring = MutableString('Dungeon')
mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)

# Test №3
mutablestring1 = MutableString('dark')
mutablestring2 = MutableString('holme')

print(mutablestring1 + mutablestring2)
print(mutablestring2 + mutablestring1)

# Test №4
mutablestring = MutableString('dungeon')

print(mutablestring)
mutablestring[0] = 'D'
mutablestring[-4] = 'G'
print(mutablestring)
