from functools import total_ordering


@total_ordering
class Word:
    """Класс описывает слово"""
    def __init__(self, word):
        self._word = word

    def __eq__(self, other):
        """self == other"""
        if isinstance(other, Word):
            return len(self._word) == len(other.word)
        else:
            return NotImplemented

    def __lt__(self, other):
        """self < other"""
        if isinstance(other, Word):
            return len(self._word) < len(other.word)
        else:
            return NotImplemented

    def __str__(self):
        return str.title(self.word)

    def __repr__(self):
        return "Word('%s')" % self.word

    @property
    def word(self):
        return self._word


# Test №1
print(Word('bee') == Word('hey'))
print(Word('bee') < Word('geek'))
print(Word('bee') > Word('geek'))
print(Word('bee') <= Word('geek'))
print(Word('bee') >= Word('gee'))

# Test №2
words = [Word('python'), Word('bee'), Word('geek')]
print(sorted(words))
print(min(words))
print(max(words))
