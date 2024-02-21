import re


class PhoneNumber:
    """Класс описывает телефонный номер"""

    def __init__(self, phone_number):
        if re.fullmatch(r'\d{10}', phone_number):
            self._phone_number = re.fullmatch(r'\d{10}', phone_number).group()
        elif re.fullmatch(r'(\d{3}\s){2}\d{4}', phone_number):
            self._phone_number = re.fullmatch(r'(\d{3}\s){2}\d{4}',
                                              phone_number).group().replace(' ', '')
        else:
            raise TypeError('Некорректный формат телефонного номера!')

    def __str__(self):
        return f'({self._phone_number[:3]}) {self._phone_number[3:6]}-{self._phone_number[6:]}'

    def __repr__(self):
        return f"PhoneNumber('{self._phone_number}')"


phone = PhoneNumber('9173963385')
print(str(phone))
print(repr(phone))

phone = PhoneNumber('918 396 3389')
print(str(phone))
print(repr(phone))
print(eval(repr(phone)))
