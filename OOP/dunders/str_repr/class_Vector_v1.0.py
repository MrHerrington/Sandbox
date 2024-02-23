class Vector:
    """Класс описывает вектор на плоскости"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self._x}, {self._y})'

    def __repr__(self):
        return f'Vector({self._x}, {self._y})'


vector = Vector(1, 2)
print(str(vector))
print(repr(vector))
print(eval(repr(vector)))
print()

vectors = [Vector(1, 2), Vector(3, 4)]
print(vectors)
