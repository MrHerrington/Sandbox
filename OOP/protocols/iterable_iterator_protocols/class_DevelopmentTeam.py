class DevelopmentTeam:
    """Класс описывает команду разработчиков"""
    def __init__(self):
        self._list = list()

    def __iter__(self):
        yield from self._list

    def add_junior(self, *args):
        self._list.extend(map(lambda x: (x, 'junior'), args))

    def add_senior(self, *args):
        self._list.extend(map(lambda x: (x, 'senior'), args))


# Test №1
dungeon = DevelopmentTeam()
dungeon.add_junior('Timur')
dungeon.add_junior('Arthur', 'Valery')
dungeon.add_senior('Gvido')
print(*dungeon, sep='\n')

# Test №2
dungeon = DevelopmentTeam()
print(len(list(dungeon)))

# Test №3
dungeon = DevelopmentTeam()
dungeon.add_junior('Timur')
dungeon.add_junior('Arthur', 'Valery')
print(*dungeon, sep='\n')
