class Vector:
    """Класс описывает вектор на плоскости"""
    version = 'v.1.1'

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
b = Vector(1, 2)
print(a == b)
print(a != b)
print(Vector.version)

# Test №2
a = Vector(1, 2)
pair1 = (1, 2)
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)
pair5 = (1, 4, 3, 2)
print(a == pair1)
print(a == pair2)
print(a == pair3)
print(a == pair4)
print(a == pair5)
