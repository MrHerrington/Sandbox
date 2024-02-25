class Logger:
    def __setattr__(self, attr, value):
        print(f'Изменение значения атрибута {attr} на {value}')
        return object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        print(f'Удаление атрибута {attr}')
        del self.__dict__[attr]


# Test №1
obj = Logger()
obj.attr = 1
del obj.attr

# Test №2
obj = Logger()
obj.name = 'pygen'
obj.rating = '5*'
obj.ceo = 'Van'
del obj.rating
obj.rating = '6*'
