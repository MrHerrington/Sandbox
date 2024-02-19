class Color:
    """Класс описывает цвет"""
    def __init__(self, hexcode):
        self._hexcode = hexcode

    @property
    def r(self):
        """Интенсивность красного компонента цвета в виде десятичного числа"""
        return int(self._hexcode[:2], base=16)

    @property
    def g(self):
        """Интенсивность зеленого компонента цвета в виде десятичного числа"""
        return int(self._hexcode[2:4], base=16)

    @property
    def b(self):
        """Интенсивность синего компонента цвета в виде десятичного числа"""
        return int(self._hexcode[4:], base=16)

    @property
    def hexcode(self):
        """Свойство возвращает шестнадцатеричное значение цвета"""
        return self._hexcode

    @hexcode.setter
    def hexcode(self, new_hexcode):
        """Свойство изменяет шестнадцатеричное значение цвета"""
        self._hexcode = new_hexcode


color = Color('0000FF')
color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)
