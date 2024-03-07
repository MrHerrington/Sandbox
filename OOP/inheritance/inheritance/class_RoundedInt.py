class RoundedInt(int):
    def __new__(cls, num, even=True):
        instance = None
        if (num % 2 and even) or (not num % 2 and not even):
            instance = num + 1
        elif (num % 2 and not even) or (not num % 2 and even):
            instance = num
        return super().__new__(cls, instance)


# Test №1
print(RoundedInt(7))
print(RoundedInt(8))
print(RoundedInt(7, False))
print(RoundedInt(8, False))

# Test №2
roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))

