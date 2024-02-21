from functools import singledispatchmethod


class IPAddress:
    """Класс описывает IP-адрес"""
    @singledispatchmethod
    def __init__(self, _ipaddress):
        raise TypeError('Неправильный тип данных')

    @__init__.register(str)
    def _(self, ipaddress):
        self._ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, ipaddress):
        self._ipaddress = '.'.join(str(i) for i in ipaddress)

    def __str__(self):
        return self._ipaddress

    def __repr__(self):
        return f"IPAddress('{self._ipaddress}')"


ip = IPAddress([1, 1, 10, 255])
print(str(ip))
print(repr(ip))
print(eval(repr(ip)))
