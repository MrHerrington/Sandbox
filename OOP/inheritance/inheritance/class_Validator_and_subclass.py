class Validator:
    def __init__(self, obj):
        self.obj = obj

    @staticmethod
    def is_valid():
        return None


class NumberValidator(Validator):
    def is_valid(self):
        return type(self.obj) in (int, float)


# Test №1
print(issubclass(NumberValidator, Validator))

# Test №2
validator1 = Validator('dungeon')
validator2 = Validator(1)
validator3 = Validator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())

# Test №3
validator1 = NumberValidator('dungeon')
validator2 = NumberValidator(1)
validator3 = NumberValidator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())
