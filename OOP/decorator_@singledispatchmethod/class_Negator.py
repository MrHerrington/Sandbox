from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(input_):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _from_int_float(input_):
        return - input_

    @neg.register(bool)
    @staticmethod
    def _from_bool(input_):
        return not input_


print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))
try:
    Negator.neg('number')
except TypeError as e:
    print(e)
