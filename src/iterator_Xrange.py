class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration
        temp = self.start
        self.start += self.step
        return temp


evens = Xrange(0, 10, 2)
print(*evens)
