class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)


# Test №1
print(issubclass(EquilateralTriangle, Triangle))

# Test №2
triangle1 = Triangle(3, 4, 5)
triangle2 = EquilateralTriangle(3)
print(triangle1.perimeter())

print(triangle2.perimeter())
