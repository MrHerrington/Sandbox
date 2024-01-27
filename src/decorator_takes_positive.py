def takes_positive(func):
    def inner(*args):
        if all(arg > 0 for arg in args):
            return func(*args)
        elif any(arg < 0 for arg in args):
            raise ValueError
        else:
            raise Exception
    return inner


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))
