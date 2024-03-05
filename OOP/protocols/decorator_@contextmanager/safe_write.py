import copy
from contextlib import contextmanager


@contextmanager
def safe_write(filename):
    file = open(filename, 'a', encoding='utf-8')
    try:
        yield file
    except Exception as error:
        print(f'Во время записи в файл было возбуждено исключение {error}')
        return file


with safe_write('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')

with safe_write('undertale.txt') as file:
    file.write('Под весёлый шорох листвы вы наполняетесь решительностью')
    raise ValueError

with open('undertale.txt', encoding='utf-8') as file:
    print(file.read())
