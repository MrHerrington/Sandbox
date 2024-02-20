from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(input_):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def _from_int_float(input_):
        return input_ * 2

    @process.register(str)
    @staticmethod
    def _from_str(input_):
        return str.upper(input_)

    @process.register(list)
    @staticmethod
    def _from_list(input_):
        return sorted(input_)

    @process.register(tuple)
    @staticmethod
    def _from_tuple(input_):
        return tuple(sorted(input_))


print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))
try:
    Processor.process({1, 2, 3})
except TypeError as e:
    print(e)
