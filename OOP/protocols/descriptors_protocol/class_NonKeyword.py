from keyword import iskeyword


class NonKeyword:
    def __init__(self, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if isinstance(value, str) and len(value) > 0 and not iskeyword(value):
            obj.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')


# Test №1
class Student:
    name = NonKeyword('name')


student = Student()
student.name = 'Peter'

print(student.name)

# Test №2
class Student:
    name = NonKeyword('name')


student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

# Test №3
class Student:
    name = NonKeyword('name')


student = Student()
student.name = 'Peter'

try:
    student.name = 'class'
except ValueError as e:
    print(e)
