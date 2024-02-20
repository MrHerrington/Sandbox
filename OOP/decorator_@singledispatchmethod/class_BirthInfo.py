from functools import singledispatchmethod
from datetime import date


class BirthInfo:
    """Класс описывает данные о дате рождения"""
    def __init__(self, birth_date):
        self._birth_date = BirthInfo.date_converter(birth_date)
        self._age = date.today()

    @property
    def birth_date(self):
        """Свойство возвращает дату рождения"""
        return self._birth_date

    @birth_date.setter
    def birth_date(self, new_birth_date):
        """Свойство изменяет дату рождения"""
        self._birth_date = BirthInfo.date_converter(new_birth_date)

    @staticmethod
    def is_isoformat(date_):
        """Метод проверяет корректность даты рождения, переданной через строку в ISO-формате"""
        try:
            return date.fromisoformat(date_)
        except ValueError:
            print('Аргумент переданного типа не поддерживается')

    @singledispatchmethod
    @staticmethod
    def date_converter(date_):
        """Базовый случай, если методу передан некорректный тип даты рождения"""
        raise TypeError('Аргумент переданного типа не поддерживается')

    @date_converter.register(date)
    @staticmethod
    def _from_date(date_):
        """Метод возвращает дату рождения без преобразования"""
        return date_

    @date_converter.register(str)
    @staticmethod
    def _from_isoformat(date_: is_isoformat):
        """Метод преобразовывает дату рождения из строки в ISO-формате в date"""
        return BirthInfo.is_isoformat(date_)

    @date_converter.register(list)
    @date_converter.register(tuple)
    @staticmethod
    def _from_list_tuple(date_):
        """Метод преобразовывает дату рождения из списка/кортежа в date"""
        return date(date_[0], date_[1], date_[-1])

    @property
    def age(self):
        """Свойство возвращает возраст объекта на текущую дату"""
        if self._age.month > self._birth_date.month:
            self._age = self._age.year - self._birth_date.year
            return self._age
        elif self._age.month == self._birth_date.month:
            if self._age.day >= self._birth_date.day:
                self._age = self._age.year - self._birth_date.year
                return self._age
        else:
            self._age = self._age.year - self._birth_date.year - 1
            return self._age


# INPUT DATA:

# TEST_1:
birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo1.age)
print(birthinfo2.birth_date)
print(birthinfo2.age)
print(birthinfo3.birth_date)
print(birthinfo3.age)

# TEST_2:
birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(type(birthinfo1.birth_date))
print(type(birthinfo2.birth_date))
print(type(birthinfo3.birth_date))

# TEST_3:
errors = [20200918, True, {1: 'one'}, {1, 2, 3}, 100.9]

for obj in errors:
    try:
        BirthInfo(obj)
    except TypeError as e:
        print(e)

# TEST_4:
birth_dates = ['20200918', '2020-0918', '202009-18', ' 2020-09-18 ', '2020-9-18']

for birth_date_ in birth_dates:
    try:
        birthinfo1 = BirthInfo(birth_date_)
    except TypeError as e:
        print(e)
