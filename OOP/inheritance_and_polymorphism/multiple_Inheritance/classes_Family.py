class Father:
    def __init__(self, mood='neutral'):
        self._mood = mood

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, new_mood):
        self._mood = new_mood

    @staticmethod
    def greet():
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'


class Mother:
    def __init__(self, mood='neutral'):
        self._mood = mood

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, new_mood):
        self._mood = new_mood

    @staticmethod
    def greet():
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass


# Test №1
father = Father()
mother = Mother()

print(father.mood)
print(mother.mood)
print(father.greet())
print(mother.greet())

# Test №2
father = Father('happy')
mother = Mother('unhappy')

print(father.mood)
print(mother.mood)

father.be_strict()
mother.be_kind()

print(father.mood)
print(mother.mood)

# Test №3
daughter = Daughter()

print(daughter.greet())
print(daughter.mood)

daughter.be_kind()
print(daughter.mood)
daughter.be_strict()
print(daughter.mood)

# Test №4
son = Son()

print(son.greet())
print(son.mood)

son.be_kind()
print(son.mood)
son.be_strict()
print(son.mood)
