class BankAccount:
    """Класс описывает банковский счет"""
    def __init__(self, balance=0):
        """balance — баланс счета, по умолчанию имеет значение 0"""
        self._balance = balance

    def get_balance(self):
        """Метод возвращает актуальный баланс счета"""
        return self._balance

    def deposit(self, amount):
        """Метод принимает в качестве аргумента число amount
        и увеличивает баланс счета на amount"""
        self._balance += amount

    def withdraw(self, amount):
        """Метод принимает в качестве аргумента число amount и уменьшает баланс счета
        на amount. Если amount превышает количество средств на балансе счета, должно быть
        возбуждено исключение ValueError с сообщением: 'На счете недостаточно средств'"""
        if amount > self._balance:
            raise ValueError('На счете недостаточно средств')
        else:
            self._balance -= amount

    def transfer(self, _account, amount):
        """Метод принимает в качестве аргументов банковский счет account и число amount.
        Метод уменьшает баланс текущего счета на amount и увеличивает баланс счета account
        на amount. Если amount превышает количество средств на балансе текущего счета, должно быть
        возбуждено исключение ValueError с сообщением: 'На счете недостаточно средств'"""
        if amount > self._balance:
            raise ValueError('На счете недостаточно средств')
        else:
            self._balance -= amount
            _account.deposit(amount)


account1 = BankAccount(100)
account2 = BankAccount(200)
account1.transfer(account2, 50)
print(account1.get_balance())
print(account2.get_balance())
