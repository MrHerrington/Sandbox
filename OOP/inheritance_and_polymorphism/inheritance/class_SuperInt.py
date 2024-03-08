class SuperInt(int):
    def __iter__(self):
        return map(type(self), str(abs(self)))

    def repeat(self, n=2):
        return type(self)(int(str(self) + str(abs(self)) * (n - 1)))

    def to_bin(self):
        return f'{self:b}'

    def next(self):
        return type(self)(self + 1)

    def prev(self):
        return type(self)(self - 1)


# Test №1
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.repeat())
print(superint2.repeat(3))

# Test №2
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.to_bin())
print(superint2.to_bin())

# Test №3
superint = SuperInt(17)

print(superint.prev())
print(superint.next())

# Test №4
superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)

print(*superint1)
print(*superint2)
