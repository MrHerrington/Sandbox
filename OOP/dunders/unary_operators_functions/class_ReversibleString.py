class ReversibleString:
    def __init__(self, str_):
        self._str_ = str_

    def __neg__(self):
        return ReversibleString(''.join(reversed(self._str_)))

    def __str__(self):
        return f'{self._str_}'


string = ReversibleString('python')
print(string)
print(-string)
