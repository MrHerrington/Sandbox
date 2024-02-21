class Rectangle:
    """Класс описывает прямоугольник"""
    def __init__(self, length, width):
        """length - длина прямоугольника,
        width - ширина пря моугольника"""
        self._length = length
        self._width = width
        self._perimeter = (self._length + self._width) * 2
        self._area = self._length * self._width

    @property
    def length(self):
        """Cвойство озвращает длину прямоугольника"""
        return self._length

    @length.setter
    def length(self, new_length):
        """Свойство изменяет длину прямоугольника"""
        self._length = new_length
        self._perimeter = (self._length + self._width) * 2
        self._area = self._length * self._width

    @property
    def width(self):
        """Свойство возвращает ширину прямоугольника"""
        return self._width

    @width.setter
    def width(self, new_width):
        """Свойствво изменяет ширину прямоугольника"""
        self._width = new_width
        self._perimeter = (self._length + self._width) * 2
        self._area = self._length * self._width

    def perimeter(self):
        """Метод возвращает периметр прямоугольника"""
        return self._perimeter

    def area(self):
        """Метод возвращает площадь прямоугольника"""
        return self._area


    @classmethod
    def square(cls, side):
        """Метод класса принимает в качестве аргумента число side и возвращает
        экземпляр класса Rectangle c длиной и шириной, равными side"""
        return cls(side, side)


rectangle = Rectangle.square(5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.area())
