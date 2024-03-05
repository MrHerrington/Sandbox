class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._name = name
        self._default = default

    def __get__(self, obj, cls):
        if self._name in obj.__dict__:
            return obj.__dict__[self._name]
        elif self._default is not None:
            return self._default
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            obj.__dict__[self._name] = value
        else:
            raise ValueError('Некорректное значение')


# Test №1
class Student:
    score = NonNegativeInteger('score')


student = Student()
student.score = 90

print(student.score)


# Test №2
class Student:
    score = NonNegativeInteger('score', 0)


student = Student()

print(student.score)
student.score = 0
print(student.score)


# Test №3
class Student:
    score = NonNegativeInteger('score')


student = Student()

try:
    print(student.score)
except AttributeError as e:
    print(e)


# Test №4
class Student:
    score = NonNegativeInteger('score')


student = Student()

try:
    student.score = -90
except ValueError as e:
    print(e)
