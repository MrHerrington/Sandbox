class HistoryDict:
    """Класс описывает словарь, который запоминает предыдущие значения по каждому ключу"""
    def __init__(self, sequence_=None):
        if sequence_ is None:
            self._sequence_ = dict()
        else:
            self._sequence_ = sequence_
        self._all_history = {k: [v] for k, v in self._sequence_.items()}

    def __len__(self):
        return len(self._sequence_)

    def __iter__(self):
        yield from self._sequence_

    def __getitem__(self, item):
        if item in self._sequence_:
            return self._sequence_[item]
        return None

    def __setitem__(self, key, value):
        self._sequence_[key] = value
        if key in self._all_history:
            self._all_history[key].append(value)
        else:
            self._all_history[key] = [value]

    def __delitem__(self, key):
        if key in self._sequence_:
            del self._sequence_[key]
            del self._all_history[key]

    def __str__(self):
        return f'{self._sequence_}'

    def __repr__(self):
        return f'HistoryDict({self._sequence_})'

    def keys(self):
        return self._sequence_.keys()

    def values(self):
        return self._sequence_.values()

    def items(self):
        return self._sequence_.items()

    def history(self, key):
        if key in self._all_history:
            return self._all_history[key]
        else:
            return list()

    def all_history(self):
        return self._all_history


# Test №1
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict['ducks'])
print(historydict['cats'])
print(len(historydict))

# Test №2
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(*historydict)
print(*historydict.keys())
print(*historydict.values())
print(*historydict.items())

# Test №3
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['ducks'] = 100
print(historydict.history('ducks'))
print(historydict.history('cats'))
print(historydict.history('dogs'))

# Test №4
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict.all_history())
historydict['ducks'] = 100
historydict['ducks'] = 101
historydict['cats'] = 2
print(historydict.all_history())

# Test №5
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['dogs'] = 1
print(len(historydict))
del historydict['ducks']
del historydict['cats']
print(len(historydict))
