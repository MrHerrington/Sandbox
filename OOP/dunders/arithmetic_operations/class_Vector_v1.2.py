class Vector:
    """Класс описывает вектор на плоскости"""
    version = 'v.1.2'

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

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


# Test №1
a = Vector(1, 2)
b = Vector(3, 4)

print(a + b)
print(a - b)
print(b + a)
print(b - a)

# Test №2
a = Vector(3, 4)
print(a * 2)
print(2 * a)
print(a / 2)
