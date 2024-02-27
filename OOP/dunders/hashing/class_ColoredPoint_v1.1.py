class ColoredPoint:
    version = '1.1'

    """Класс описывает цветную точку на плоскости"""

    def __init__(self, x, y, color=(0, 0, 0)):
        self._x = x
        self._y = y
        self._color = color

    def __eq__(self, other):
        return self._fields == other._fields

    def __hash__(self):
        return hash(self._fields)

    def __repr__(self):
        return f'ColoredPoint({self.x}, {self.y}, {self.color})'

    def __pos__(self):
        return ColoredPoint(self.x, self.y)

    def __neg__(self):
        return ColoredPoint(-self.x, -self.y)

    def __invert__(self):
        return ColoredPoint(self.y, self.x,
                            (255 - self._color[0], 255 - self._color[1], 255 - self._color[-1]))

    def __str__(self):
        return f'{self.x, self.y, self.color}'

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @property
    def _fields(self):
        return self.x, self.y, self.color


# Test №1
point1 = ColoredPoint(1, 2, 'white')
point2 = ColoredPoint(1, 2, 'white')
point3 = ColoredPoint(3, 4, 'black')

print(point1 == point2)
print(hash(point1) == hash(point2))
print(point1 == point3)
print(hash(point1) == hash(point3))

# Test №2
points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2,'black'): 20}
print(points)

# Test №3
point = ColoredPoint(1, 2, 'white')

try:
    point.color = 'black'
except AttributeError as e:
    print('Error')
