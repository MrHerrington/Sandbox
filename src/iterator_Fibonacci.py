class Fibonacci:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        self.value = lambda x: 1 if x in (1, 2) else self.value(x - 2) + self.value(x - 1)
        return self.value(self.num)


fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
