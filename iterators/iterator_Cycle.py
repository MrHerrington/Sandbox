class Cycle:
    def __init__(self, _str):
        self._str = _str
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self._str):
            self.index = 0
        value = self._str[self.index]
        self.index += 1
        return value


cycle = Cycle('be')
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
