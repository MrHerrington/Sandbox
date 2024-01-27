import string


def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')


def verification(login, password, func1, func2):
    """
    Функция проверяет правильность введенного пароля.

    Если пароль не удовлетворяет нескольким условиям, то приоритеты выбора строки-сообщения
    об ошибке являются следующими:
    - в пароле нет ни одной буквы,
    - в пароле нет ни одной заглавной буквы,
    - в пароле нет ни одной строчной буквы,
    - в пароле нет ни одной цифры
    """
    messages = dict()
    message = ''

    uppercase_check = any(i in string.ascii_uppercase for i in password)
    if not uppercase_check:
        messages[uppercase_check] = 'в пароле нет ни одной заглавной буквы'
    lowercase_check = any(i in string.ascii_lowercase for i in password)
    if not lowercase_check:
        messages[lowercase_check] = 'в пароле нет ни одной строчной буквы'
    letters_check = any((uppercase_check, lowercase_check))
    if not letters_check:
        messages[letters_check] = 'в пароле нет ни одной буквы'
    digits_check = any(i in string.digits for i in password)
    if not digits_check:
        messages[digits_check] = 'в пароле нет ни одной цифры'

    for i in (letters_check, uppercase_check, lowercase_check, digits_check):
        if not i:
            message = messages[i]
            break

    if all((uppercase_check, lowercase_check, uppercase_check, digits_check)):
        func1(login)
    else:
        func2(login, message)


verification('Ruslan_Chaniev', 'Stepikstepik2', success, failure)
