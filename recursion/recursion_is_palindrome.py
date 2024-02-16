def is_palindrome(s):
    """
    Рекурсивная функция, является ли строка палиндромом или нет
    """
    try:
        if s[0] == s[-1] and len(s) <= 2:
            return True
        else:
            if s[0] == s[-1]:
                s = s[1:-1]
                return is_palindrome(s)
            else:
                return False
    except IndexError:
        return 'Пустая строка!'


print(is_palindrome(''))
