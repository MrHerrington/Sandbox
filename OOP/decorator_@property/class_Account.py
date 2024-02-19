from hashlib import sha256


class Account:
    """Класс описывает аккаунта пользователя некоторого интернет-сервиса"""
    def __init__(self, login, password, base):
        self._base = base
        self._login = login
        self.password = password
        self._base.add(sha256(self.password.encode('utf-8')).hexdigest())

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        raise ValueError('Изменение логина невозможно')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        if sha256(new_password.encode('utf-8')).hexdigest() not in self._base:
            self._base.add(sha256(new_password.encode('utf-8')).hexdigest())
            self._password = new_password
        else:
            raise ValueError('Такой пароль уже используется')


passwords_base = set()

account_1 = Account('Billy', 'Dungeon_master', passwords_base)
print(account_1.login)
print(account_1.password)
print(account_1.__dict__)
account_1.password = 'notJabroni'
print(account_1.password)
print(account_1.__dict__)
account_1.login = 'Van'
