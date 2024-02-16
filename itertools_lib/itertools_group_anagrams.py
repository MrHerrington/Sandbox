from itertools import groupby


def group_anagrams(_iterable):
    """Функция группирует в кортежи слова из списка words, являющиеся анаграммами,
    и возвращает список полученных кортежей."""

    def comparison_key(word, dct=None):
        if dct is None:
            dct = dict()
        for letter in word:
            dct[letter] = dct.get(letter, 0) + 1
        return {key: value for key, value in sorted(dct.items())}

    sorted_iterable = sorted(_iterable, key=lambda x: sorted(comparison_key(x)))
    groupped_iterable = groupby(sorted_iterable, key=lambda x: comparison_key(x))
    for keys, values in groupped_iterable:
        yield tuple(values)


groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])
print(*groups)
