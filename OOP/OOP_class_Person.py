class Person:
    """Класс описывает человека"""
    def __init__(self, name, surname):
        """name - имя человека; surname - фамилия человека, _cache - кэш для значений fullname"""
        self._name = name
        self._surname = surname
        self._cache = dict()

    def get_name(self):
        """Метод возвращает имя человека"""
        return self._name

    def set_name(self, new_name):
        """Метод изменяет имя человека"""
        self._name = new_name

    def get_surname(self):
        """Метод возвращает фамилию человека"""
        return self._surname

    def set_surname(self, new_surname):
        """Метод изменяет фамилию человека"""
        self._surname = new_surname

    def get_fullname(self):
        """Возвращает полное имя человека из кэша (если содержится в кэше),
        или при выполнении метода с занесением в кэш"""
        if (self._name, self._surname) not in self._cache:
            _cache = self._name + ' ' + self._surname
            self._cache[(self._name, self._surname)] = _cache
            return _cache
        else:
            return self._cache[(self._name, self._surname)]

    name = property(get_name, set_name)
    surname = property(get_surname, set_surname)
    fullname = property(get_fullname)


person = Person('Меган', 'Фокс')

print(person.fullname)
person.name = 'Стефани'
print(person.fullname)
