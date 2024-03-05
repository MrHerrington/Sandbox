class MaxCallsException(BaseException):
    pass


class LimitedTakes:
    def __init__(self, attr):
        self._attr = attr
        self._times = 0

    def __get__(self, obj, cls):
        if self._times == self._attr:
            raise MaxCallsException('Превышено количество доступных обращений')
        if self._attr in obj.__dict__:
            self._times += 1
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if isinstance(value, str) and len(value) > 0:
            obj.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')


class Student:
    name = LimitedTakes(3)


student = Student()

student.name = 'Gwen'

print(student.name)
print(student.name)
print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)
