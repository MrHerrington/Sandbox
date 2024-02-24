class SuperString:
    def __init__(self, string):
        self.string = string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        else:
            return NotImplemented

    def __mul__(self, other):
        return SuperString(self.string * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return SuperString(self.string[:int(len(self.string) / other)])

    def __lshift__(self, other):
        """Метод возвращает результат побитового сдвига влево"""
        return SuperString(self.string[:(other - 1)])

    def __rshift__(self, other):
        """Метод возвращает результат побитового сдвига вправо"""
        return SuperString(self.string[other:])

    def __str__(self):
        return f'{self.string}'


# Test №1
s1 = SuperString('bee')
s2 = SuperString('geek')

print(s1 + s2)
print(s2 + s1)

# Test №2
s = SuperString('beegeek')

print(s * 2)
print(3 * s)
print(s / 3)

# Test №3
s = SuperString('beegeek')

print(s << 4)
print(s >> 3)
