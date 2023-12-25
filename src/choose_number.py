from random import *


try_counter = 0
print('Добро пожаловать в числовую угадайку')
edge = int(input('Задайте максимальную границу значения: '))
number = randint(1, edge)


def is_valid(num):
    if num.isalpha():
        return False
    elif num.isdigit():
        if 1 <= int(num) <= 100:
            return True
        else:
            return False


while True:
    num = input('Введите число от 1 до {}: '.format(edge))
    if is_valid(num):
        num = int(num)
        try_counter += 1
    else:
        print('А может быть все-таки введем целое число от 1 до 100')
        continue
    if num < number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        continue
    elif num > number:
        print('Ваше число больше загаданного, попробуйте еще разок')
        continue
    elif num == number:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        print(f'Количество ваших попыток {try_counter}.')
        play = str(input('Хотите сыграть снова? д / любой символ: '))
    if play == 'д':
        try_counter = 0
        edge = int(input('Задайте максимальную границу значения: '))
        number = randint(1, edge)
        continue
    else:
        break
