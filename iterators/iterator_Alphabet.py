class Alphabet:
    def __init__(self, language):
        self.language = language
        self.index = 0
        self.ru_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        self.en_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.dct = {'ru': self.ru_alphabet,
                    'en': self.en_alphabet}

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dct[self.language]):
            self.index = 0
        value = self.dct[self.language][self.index]
        self.index += 1
        return value


ru_alpha = Alphabet('ru')
print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))
print()


en_alpha = Alphabet('en')
letters = [next(en_alpha) for _ in range(40)]
print(*letters)
