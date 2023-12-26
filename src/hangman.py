"""Виселица / hangman"""
import os
from random import *


word_list = ['понятие', 'строительство']    # малый словарь для быстрой отладки


def get_word():
    word = choice(word_list)
    word = str(word).upper()
    return word


def display_hangman(tries):
    stages = [
    # использование символа сырых строк, чтобы не экранировать символ экранирования)
    r'''
       |------|
       |      |
       |      0
       |     /|\
       |     / \
     __|__   ''',

    r'''
       |------|
       |      |
       |      0
       |     /|\
       |     /
     __|__   ''',

    r'''
       |------|
       |      |
       |      0
       |     /|\
       |
     __|__   ''',

    r'''
       |------|
       |      |
       |      0
       |     /|
       |
     __|__   ''',


    r'''
       |------|
       |      |
       |      0
       |      |
       |
     __|__   ''',

    r'''
       |------|
       |      |
       |      0
       |
       |
     __|__   ''',

    r'''
       |------|
       |      |
       |
       |
       |
     __|__   '''

    ]
    return stages[tries]


def play(word):
    word_completion = ['_'] * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    while tries >= 0:
        os.system('cls')
        print(display_hangman(tries))
        print(*word_completion, sep='')
        print(f'Осталось {tries} попыток.')
        if tries == 0:
            print(f'Игра окончена! Загаданное слово: {word}')
            break
        s = str(input('Введите букву или слово целиком: ')).upper()
        if s.isalpha():     # проверка на ввод допустимых символов
            pass
        elif not s.isalpha():
            print('Нужно вводить только буквы!')
            continue
        if len(s) == 1 and s not in guessed_letters and s in word:  # проверка, если введена одна буква
            guessed_letters.append(s)
            tries -= 1
            for i in range(len(word)):
                if word[i] == s:
                    word_completion[i] = s
            continue
        elif len(s) == 1 and s not in guessed_letters:
            guessed_letters.append(s)
            tries -= 1
            continue
        elif len(s) == 1 and s in guessed_letters:
            print('Введена уже названная буква!')
            continue
        if len(s) > 1 and s == word:    # проверка, если введено слово целиком
            print('Поздравляем, вы угадали слово! Вы победили!')
            break
        elif len(s) > 1 and s not in guessed_words:
            guessed_words.append(s)
            tries -= 1
            continue
        elif len(s) > 1 and s in guessed_words:
            print('Введено уже названное слово!')
            continue
    print('Сыграть снова? д / н')


while True:     # основной цикл программы
    play(get_word())
    if str(input()) == 'д':
        continue
    else:
        print('Выход из программы')
        break
