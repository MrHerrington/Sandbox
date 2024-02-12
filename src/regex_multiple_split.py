import re


def multiple_split(_str, _delimeters):
    """Функция разбивает строку _str на подстроки, используя в качестве разделителей
    строки из списка  _delimiters, и возвращает полученный результат в виде списка"""
    return re.split('|'.join(map(re.escape, _delimeters)), _str)


print(multiple_split('beegeek-python.stepik', ['.', '-']))
print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))
