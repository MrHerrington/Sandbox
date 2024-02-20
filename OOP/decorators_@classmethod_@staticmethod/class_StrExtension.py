class StrExtension:
    """Класс описывает набор функций для работы со строками"""
    @staticmethod
    def remove_vowels(str_):
        """Метод удаляет из строки все гласные латинские буквы
        без учета регистра и возвращает полученный результат"""
        return ''.join(filter(lambda x: x.lower() not in 'aeiouy', str_))

    @staticmethod
    def leave_alpha(str_):
        """Метод удаляет из строки все символы, не являющиеся
        латинскими буквами и возвращает полученный результат"""
        return ''.join(filter(str.isalpha, str_))

    @staticmethod
    def replace_all(string_, chars, char):
        """Метод заменяет в строке все символы из chars на char
        с учетом регистра и возвращает полученный результат"""
        return ''.join(map(lambda x: str.replace(x, x, char) if x in chars else x, string_))


print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))
print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))
print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
