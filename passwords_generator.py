from random import *


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
excpt = 'il1Lo0O'
chars = []
passwords_quantity = int(input('Количество паролей для генерации: '))
password_length = int(input('Длина одного пароля: '))
check_digits = str(input('Включая цифры? д / любой символ '))
check_lowercase = str(input('Включая прописные буквы? д / любой символ '))
check_capitals = str(input('Включая заглавные буквы? д / любой символ '))
check_symbols = str(input('Включая символы? д / любой символ '))
check_excpt = str(input('Включая неоднозначные символы? д / любой символ '))
if check_digits == 'д':
    chars.extend(digits)
if check_lowercase == 'д':
    chars.extend(lowercase_letters)
if check_capitals == 'д':
    chars.extend(uppercase_letters)
if check_symbols == 'д':
    chars.extend(punctuation)
if check_excpt == 'д':
    pass
else:
    for i in excpt:
        if i in chars:
            chars.remove(i)


def generate_password(a, b):
    for _ in range(a):
        password = ''
        for j in range(b):
            password = password + choice(chars)
        yield password


print(*generate_password(passwords_quantity, password_length), sep='\n')
