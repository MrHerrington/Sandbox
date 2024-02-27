class ColoredPoint:
    version = '1.0'

    """Класс описывает цветную точку на плоскости"""
    def __init__(self, x, y, color=(0, 0, 0)):
        self._x = x
        self._y = y
        self._color = color

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


# Test №1
point = ColoredPoint(2, -3)

print(+point)
print(-point)
print(~point)

# Test №2
point1 = ColoredPoint(2, -3)
point2 = ColoredPoint(10, 20, (34, 45, 67))

print(point1.color)
print(point2.color)
