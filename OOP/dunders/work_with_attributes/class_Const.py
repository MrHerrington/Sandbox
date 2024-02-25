class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, attr, value):
        if attr not in self.__dict__:
            self.__dict__[attr] = value
        else:
            raise AttributeError('Изменение значения атрибута невозможно')

    def __delattr__(self, attr):
        raise AttributeError('Удаление атрибута невозможно')


# Test №1
videogame = Const(name='Cuphead')

videogame.developer = 'Studio MDHR'
print(videogame.name)
print(videogame.developer)

# Test №2
videogame = Const(name='Dicso Elysium')

try:
    videogame.name = 'Half-Life: Alyx'
except AttributeError as e:
    print(e)

# Test №3
videogame = Const(name='The Last of Us')

try:
    del videogame.name
except AttributeError as e:
    print(e)
