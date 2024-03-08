class Counter:
    def __init__(self, start=0):
        self.start = start

    @property
    def value(self):
        return self.start

    def inc(self, n=1):
        self.start += n

    def dec(self, n=1):
        if self.start - n < 0:
            self.start = 0
        else:
            self.start -= n


class NonDecCounter(Counter):
    def dec(self, n=1):
        pass


class LimitedCounter(Counter):
    def inc(self, n=1, limit=10):
        if self.start + n > limit:
            self.start = limit
        else:
            self.start += n


# Test №1
print(issubclass(NonDecCounter, Counter))
print(issubclass(LimitedCounter, Counter))

# Test №2
counter = Counter()
print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(3)
print(counter.value)
counter.dec(10)
print(counter.value)

# Test №3
counter = NonDecCounter(10)
print(counter.value)
counter.inc()
counter.inc(10)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(50)
print(counter.value)

# Test №4
counter = LimitedCounter()
print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)
