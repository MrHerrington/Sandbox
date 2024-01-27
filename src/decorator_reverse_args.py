def reverse_args(func):
    def inner(*args):
        args = args[::-1]
        return func(*args)
    return inner


@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))
