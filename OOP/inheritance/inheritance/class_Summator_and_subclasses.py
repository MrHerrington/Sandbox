class Summator:
    @staticmethod
    def total(n, degree=1):
        return sum(i ** degree for i in range(1, n + 1))


class SquareSummator(Summator):
    @staticmethod
    def total(n, degree=2):
        return sum(i ** degree for i in range(1, n + 1))


class QubeSummator(Summator):
    @staticmethod
    def total(n, degree=3):
        return sum(i ** degree for i in range(1, n + 1))


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n, degree=2):
        return sum(i ** self.m for i in range(1, n + 1))


# Test №1
print(issubclass(SquareSummator, Summator))
print(issubclass(QubeSummator, Summator))

# Test №2
summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))  # 1 + 2 + 3
print(summator2.total(3))  # 1 + 4 + 9
print(summator3.total(3))  # 1 + 8 + 27

# Test №3
summator1 = Summator()
summator2 = CustomSummator(2)
summator3 = CustomSummator(3)

print(summator1.total(3))  # 1 + 2 + 3
print(summator2.total(3))  # 1 + 4 + 9
print(summator3.total(3))  # 1 + 8 + 27
