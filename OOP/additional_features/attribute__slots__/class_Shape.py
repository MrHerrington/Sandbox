from functools import total_ordering


@total_ordering
class Shape:
    __slots__ = ('name', 'color', 'area')

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f'{self.name} {self.color} ({self.area})'

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area


# Test №1
shape = Shape('triangle', 'red', 12)

print(shape.name)
print(shape.color)
print(shape.area)

# Test №2
print(Shape('Square', 'Red', 4))

# Test №3
print(Shape('rectangle', 'green', 12) == Shape('triangle', 'red', 12))
print(Shape('triangle', 'red', 15) > Shape('triangle', 'red', 12))

# Test №4
shape = Shape('triangle', 'red', 12)

try:
    shape.perimeter = 9
except AttributeError:
    print('Error')

# Test №5
shape = Shape('triangle', 'red', 12)

print(shape.__slots__)
print(shape.__dict__)
