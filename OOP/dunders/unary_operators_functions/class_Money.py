class Money:
    def __init__(self, money):
        self._money = money

    def __pos__(self):
        return Money(self._money)

    def __neg__(self):
        return Money(-self._money)

    def __str__(self):
        return f'{self._money} руб.'


money = Money(100)

print(money)
print(+money)
print(-money)
