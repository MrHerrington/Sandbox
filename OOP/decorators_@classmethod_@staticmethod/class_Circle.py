class Circle:
    """Класс описывает круг"""
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius

    @classmethod
    def from_diameter(cls, diameter):
        """Метод класса принимает в качестве аргумента диаметр круга и возвращает
        экземпляр класса Circle, созданный на основе переданного диаметра"""
        return cls(diameter / 2)


circle = Circle.from_diameter(10)
print(circle.radius)
