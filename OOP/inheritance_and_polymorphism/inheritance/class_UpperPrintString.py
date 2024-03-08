class UpperPrintString(str):
    def __str__(self):
        return super().__str__().upper()


# Test №1
s1 = UpperPrintString('dungeon')
s2 = UpperPrintString('DunGeon')
print(s1)
print(s2)

# Test №2
s = UpperPrintString('dungeon')
print(list(s))
