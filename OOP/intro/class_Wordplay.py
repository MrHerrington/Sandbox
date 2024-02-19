from itertools import filterfalse


class Wordplay:
    """Класс описывает расширяемый набор слов"""
    def __init__(self, words=None):
        """words - список, определяющий начальный набор слов, если не передан,
        начальный набор слов считается пустым"""
        if words is None:
            self.words = list()
        else:
            self.words = words

    def add_word(self, word):
        """Метод принимает в качестве аргумента слово и добавляет его в набор.
        Если слово уже есть в наборе, метод ничего не делает"""
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, length):
        """Метод принимает в качестве аргумента натуральное число length
        и возвращает список слов из набора, длина которых равна length"""
        return list(filter(lambda x: len(x) == length, self.words))

    def only(self, *args):
        """Метод принимает произвольное количество аргументов — букв, и возвращает
        все слова из набора, которые включают в себя только переданные буквы"""
        return list(filter(lambda x: all(j in args for i in x for j in i), self.words))

    def avoid(self, *args):
        """Метод принимает произвольное количество аргументов — букв, и возвращает
        все слова из списка words, которые не содержат ни одну из этих букв"""
        return list(filterfalse(lambda x: any(j in args for i in x for j in i), self.words))


wordplay = Wordplay(['o', 'to', 'otto', 'rap', 't'])

print(wordplay.only('o', 't'))
print(wordplay.avoid('o', 't'))
