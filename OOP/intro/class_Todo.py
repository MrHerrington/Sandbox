class Todo:
    """Класс описывает список дел"""
    def __init__(self):
        """things — изначально пустой список дел, которые нужно выполнить"""
        self.things = []

    def add(self, _todo, priority):
        """Метод принимает название дела и его приоритет и
        добавляет данное дело в список дел в виде кортежа"""
        self.things.append((_todo, priority))

    def get_by_priority(self, n):
        """Метод принимает в качестве аргумента целое число n
        и возвращает список названий дел, имеющих приоритет n"""
        return list(map(lambda x: x[0],
                        filter(lambda y: int(y[-1]) == int(n), self.things)))

    def get_low_priority(self):
        """Метод возвращает список названий дел, имеющих самый низкий приоритет"""
        return list(map(lambda x: x[0],
                        filter(lambda y: int(y[-1]) == min(map(lambda z: z[-1], self.things)), self.things)))

    def get_high_priority(self):
        """Метод возвращает список названий дел, имеющих самый высокий приоритет"""
        return list(map(lambda x: x[0],
                        filter(lambda y: int(y[-1]) == max(map(lambda z: z[-1], self.things)), self.things)))


todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))
print(Todo.__doc__)
print(Todo.get_low_priority.__doc__)
