class Rectangle:
    """Класс описывает прямоугольник"""
    def __init__(self, length, width):
        """length - длина прямоугольника,
        width - ширина прямоугольника"""
        self._length = length
        self._width = width
        self._perimeter = (self._length + self._width) * 2
        self._area = self._length * self._width

    def get_length(self):
        """Возвращает длину прямоугольника"""
        return self._length

    def set_length(self, new_length):
        """Изменяет длину прямоугольника"""
        self._length = new_length
        self._perimeter = (self._length + self._width) * 2
        self._area = self._length * self._width

    def get_width(self):
        """Возвращает ширину прямоугольника"""
        return self._width

    def set_width(self, new_width):
        """Изменяет ширину прямоугольника"""
        self._width = new_width
        self._perimeter = (self._length + self._width) * 2
        self._area = self._length * self._width

    def perimeter(self):
        """Возвращает периметр прямоугольника"""
        return self._perimeter

    def area(self):
        """Возвращает площадь прямоугольника"""
        return self._area

    length = property(get_length, set_length)
    width = property(get_width, set_width)
    perimeter = property(perimeter)
    area = property(area)


rec = Rectangle(4, 5)

print(rec.length)
print(rec.width)
print(rec.perimeter)
print(rec.area)

rec.length = 6
print(rec.length)
print(rec.width)
print(rec.perimeter)
print(rec.area)
