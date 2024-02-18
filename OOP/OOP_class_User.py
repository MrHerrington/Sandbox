class User:
    """Класс описывает интернет пользователя"""
    def __init__(self, name, age):
        """_name - имя пользователя (непустая строка из буквенных символов),
        _age - возраст пользователя (число от 0 до 110 включительно)"""
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')
        if isinstance(age, int) and -1 < age < 111:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')

    def get_name(self):
        """Метод возвращает имя пользователя"""
        return self._name

    def set_name(self, new_name):
        """Метод принимает в качестве аргумента допустимое значение
        new_name и изменяет имя пользователя на new_name."""
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError('Некорректное имя')

    def get_age(self):
        """Метод возвращает возраст пользователя"""
        return self._age

    def set_age(self, new_age):
        """Метод принимает в качестве аргумента допустимое значение
        new_age и изменяет возраст пользователя на new_age."""
        if isinstance(new_age, int) and -1 < new_age < 111:
            self._age = new_age
        else:
            raise ValueError('Некорректный возраст')

    name = property(get_name, set_name)
    age = property(get_age, set_age)


user = User('Гвидо', 67)

print(user.name)
user.name = 'Тимур'
print(user.name)
