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

    def __pos__(self):
        return Vector(self.x, self.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

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


vector = Vector(3, -4)
print(+vector)
print(-vector)
print(abs(vector))
