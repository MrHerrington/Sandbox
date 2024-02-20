from functools import singledispatchmethod


class Formatter:
    """Класс описывает тип данных принимаемых аргументов"""
    @singledispatchmethod
    @staticmethod
    def format(input_):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def _from_int(input_):
        return f'Целое число: {input_}'

    @format.register(float)
    @staticmethod
    def _from_float(input_):
        return 'Вещественное число: {}'.format(input_)

    @format.register(tuple)
    @staticmethod
    def _from_tuple(input_):
        return 'Элементы кортежа: {0}'.format(', '.join(map(str, input_)))

    @format.register(list)
    @staticmethod
    def _from_list(input_):
        return 'Элементы списка: {elements}'.format(elements=', '.join(map(str, input_)))

    @format.register(dict)
    @staticmethod
    def _from_dict(input_):
        return 'Пары словаря: %s' % ', '.join(str((k, v)) for k, v in input_.items())


print(Formatter.format(1337))
print(Formatter.format(20.77))
print(Formatter.format([10, 20, 30, 40, 50]))
print(Formatter.format(([1, 3], [2, 4, 6])))
print(Formatter.format({'Cuphead': 1, 'Mugman': 3}))
print(Formatter.format({1: 'one', 2: 'two'}))
print(Formatter.format({1: True, 0: False}))
try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)
