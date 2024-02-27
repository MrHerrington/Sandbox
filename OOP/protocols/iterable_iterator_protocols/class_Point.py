class Point:
    """Класс описывает точку в пространстве"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Point({self.x}, {self.y}, {self.z})'

    def __iter__(self):
        yield from (self.x, self.y, self.z)


# Test №1
point = Point(1, 2, 3)
print(list(point))

# Test №2
point = Point(1, 2, 3)
x, y, z = point
print(x, y, z)

# Test №3
points = [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]
print(points)
