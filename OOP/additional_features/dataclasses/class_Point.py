from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(default=0, compare=False)

    def __post_init__(self):
        dct_quadrant = {
            (True, True): 1,
            (False, True): 2,
            (False, False): 3,
            (True, False): 4
        }
        if self.x or self.y:
            self.quadrant = dct_quadrant[(self.x > 0, self.y > 0)]

    def symmetric_x(self):
        return type(self)(self.x, -self.y)

    def symmetric_y(self):
        return type(self)(-self.x, self.y)


# Test №1
point = Point()

print(point)
print(point.x)
print(point.y)
print(point.quadrant)

# Test №2
point = Point(1.0, 2.0)
print(point.symmetric_x())
print(point.symmetric_y())

# Test №3
point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(3, 4)

print(point1 == point2)
print(point1 == point3)
print(point2 != point3)
