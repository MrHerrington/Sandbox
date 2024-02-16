class Square:
    def __init__(self, n):
        self.n = n
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.n:
            raise StopIteration
        temp = self.start ** 2
        self.start += 1

        return temp


squares = Square(10)
print(list(squares))
