def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper


@do_twice
def beegeek():
    print('beegeek')


print(beegeek())
