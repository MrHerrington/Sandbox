class Pet:
    """Класс описывает домашнее животное"""
    pet_list = list()

    def __init__(self, name):
        self._name = name
        Pet.pet_list.append(self)

    @property
    def name(self):
        """Свойство возвращает имя животного"""
        return self._name

    @name.setter
    def name(self, new_name):
        """Свойство изменяет имя животного"""
        self._name = new_name

    @classmethod
    def first_pet(cls):
        """Метод класса возвращает имя первого животного"""
        try:
            return cls.pet_list[0]
        except IndexError:
            pass

    @classmethod
    def last_pet(cls):
        """Метод класса возвращает имя последнего животного"""
        try:
            return cls.pet_list[-1]
        except IndexError:
            pass

    @classmethod
    def num_of_pets(cls):
        """Метод класса возвращает общее количество животных"""
        return len(cls.pet_list)


pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')
pet1.name = 'Boychik'
print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
