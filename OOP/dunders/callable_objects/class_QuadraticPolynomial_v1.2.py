from collections import namedtuple


class QuadraticPolynomial:
    """Класс описывает квадратный трехчлен"""
    version = '1.2'

    def __init__(self, a=0, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    @property
    def a(self):
        """Свойство возвращает значение коэффициента a"""
        return self._a

    @a.setter
    def a(self, a):
        """Свойство изменяет значение коэффициента a"""
        self._a = a

    @property
    def b(self):
        """Свойство возвращает значение коэффициента b"""
        return self._b

    @b.setter
    def b(self, b):
        """Свойство изменяет значение коэффициента b"""
        self._b = b

    @property
    def c(self):
        """Свойство возвращает значение коэффициента c"""
        return self._c

    @c.setter
    def c(self, c):
        """Свойство изменяет значение коэффициента c"""
        self._c = c

    @property
    def x1(self):
        """Свойство возвращает первый корень, если дискриминант больше или равен 0"""
        d = self._b ** 2 - 4 * self._a * self._c
        if d > -1:
            return round((-self._b - d**0.5) / 2 / self._a, 3)

    @property
    def x2(self):
        """Свойство возвращает второй корень, если дискриминант больше или равен 0"""
        d = self._b ** 2 - 4 * self._a * self._c
        if d > -1:
            return round((-self._b + d ** 0.5) / 2 / self._a, 3)

    @property
    def view(self):
        """Свойство возвращает общий вид квадратного уравнения"""
        if self._a != 0:
            view_a = f'{self._a}x^2'
        else:
            view_a = ''
        if self._b > 0:
            if view_a:
                view_b = f' + {self._b}x'
            else:
                view_b = f'{self._b}x'
        elif self._b < 0:
            view_b = f' - {abs(self._b)}x'
        else:
            view_b = ''
        if self._c > 0:
            if view_a or view_b:
                view_c = f' + {self._c}'
            else:
                view_c = f'{self._c}'
        elif self._c < 0:
            view_c = f' - {abs(self._c)}'
        else:
            view_c = ''
        return view_a + view_b + view_c

    @property
    def coefficients(self):
        """Свойство возвращает коэффициенты в виде кортежа"""
        return self._a, self._b, self._c

    @coefficients.setter
    def coefficients(self, new_coefficients):
        self._a = new_coefficients[0]
        self._b = new_coefficients[1]
        self._c = new_coefficients[-1]

    @classmethod
    def from_iterable(cls, iterable_):
        """Метод класса возвращает экземпляр класса на основе аргументов,
        переданных в iterable_"""
        return cls(iterable_[0], iterable_[1], iterable_[-1])

    @classmethod
    def from_str(cls, str_):
        """Метод класса возвращает экземпляр класса на основе аргументов,
        переданных с помощью строки и преобразованных в float"""
        Arguments = namedtuple('Arguments', 'a b c')
        arguments = Arguments(*cls.from_str_to_arguments(str_))
        return cls(arguments.a, arguments.b, arguments.c)

    @staticmethod
    def from_str_to_arguments(str_):
        """Вспомогательный метод, преобразовывает аргументы,
        переданные в строке, в тип float"""
        return list(map(float, str_.split()))


# Test №1
func = QuadraticPolynomial(1, 2, 1)
print(func(1))
print(func(2))

# Test №2
func = QuadraticPolynomial(1, 3, 4)
print(func(1))
print(func(2))
print(QuadraticPolynomial.version)
