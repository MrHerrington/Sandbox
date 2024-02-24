class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = dict()

    def __call__(self, *args):
        if tuple(args) not in self.cache:
            temp = self.func(*args)
            self.cache[tuple(args)] = temp
            return temp
        else:
            return self.cache[tuple(args)]


# Test №1
@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


print(slow_fibonacci(100))


# Test №2
@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


slow_fibonacci(5)
for args, value in sorted(slow_fibonacci.cache.items()):
    print(args, value)
