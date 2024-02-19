class Person:
    """Класс описывает человека"""
    def __init__(self, name, surname):
        """name - имя человека; surname - фамилия человека, _cache - кэш для значений fullname"""
        self._name = name
        self._surname = surname
        self._cache = dict()
        self._cache[(self._name, self._surname)] = self._name + ' ' + self._surname

    @property
    def name(self):
        """Метод возвращает имя человека"""
        return self._name

    @name.setter
    def name(self, new_name):
        """Метод изменяет имя человека"""
        self._name = new_name

    @property
    def surname(self):
        """Метод возвращает фамилию человека"""
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        """Метод изменяет фамилию человека"""
        self._surname = new_surname

    @property
    def fullname(self):
        """Возвращает полное имя человека из кэша (если содержится в кэше),
        или при выполнении метода с занесением в кэш"""
        if (self._name, self._surname) not in self._cache:
            _cache = self._name + ' ' + self._surname
            self._cache[(self._name, self._surname)] = _cache
            return _cache
        else:
            return self._cache[(self._name, self._surname)]

    @fullname.setter
    def fullname(self, new_fullname):
        self._name, self._surname = new_fullname.split()


person = Person('Mike', 'Pondsmith')

person.fullname = 'Troy Baker'
print(person.name)
print(person.surname)
