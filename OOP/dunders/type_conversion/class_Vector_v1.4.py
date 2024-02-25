class Vector:
    """Класс описывает вектор на плоскости"""
    version = 'v.1.4'

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        """self == other"""
        if isinstance(other, Vector):
            return self._x == other.x and self._y == other.y
        elif isinstance(other, tuple):
            return self._x == other[0] and self._y == other[-1] and len(other) == 2
        else:
            return NotImplemented

    def __pos__(self):
        return Vector(self.x, self.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        """other.__mul__(self)"""
        return self.__mul__(other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self._x}, {self._y})'

    def __repr__(self):
        return f'Vector({self._x}, {self._y})'

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __int__(self):
        return int(self.__abs__())

    def __float__(self):
        return float(self.__abs__())

    def __complex__(self):
        return complex(self.x, self.y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


# Test №1
vector = Vector(3, 4)

print(vector)
print(int(vector))
print(float(vector))
print(complex(vector))

# Test №2
print(bool(Vector(1, 2)))
print(bool(Vector(1, 0)))
print(bool(Vector(0, 1)))
print(bool(Vector(0, 0)))
