class FoodInfo:
    """Класс описывает пищевую ценность продуктов"""
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.proteins + other.proteins,
                            self.fats + other.fats,
                            self.carbohydrates + other.carbohydrates)
        else:
            return NotImplemented

    def __mul__(self, other):
        return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)

    def __truediv__(self, other):
        return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)

    def __floordiv__(self, other):
        return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)

    def __str__(self):
        return f'FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})'


# Test №1
food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 10, 20)
print(food1 + food2)
print(food1 * 2)
print(food1 / 2)
print(food1 // 2)

# Test №2
food1 = FoodInfo(10, 20, 30)
try:
    food2 = (5, 10, 15) + food1
except TypeError:
    print('Некорректный тип данных')
