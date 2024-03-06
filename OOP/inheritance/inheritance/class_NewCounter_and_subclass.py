class NewCounter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        if self.value - n < 0:
            self.value = 0
        else:
            self.value -= n


class DoubledCounter(NewCounter):
    def inc(self, n=1):
        self.value += 2 * n

    def dec(self, n=1):
        if self.value - 2 * n < 0:
            self.value = 0
        else:
            self.value -= 2 * n


# Test №1
print(issubclass(DoubledCounter, NewCounter))

# Test №2
counter = NewCounter(10)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)

# Test №3
counter = DoubledCounter(20)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)
