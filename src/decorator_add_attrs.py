def add_attrs(**attrs):
    def decorator(func):
        for keys, values in attrs.items():
            func.__dict__[keys] = values
        return func
    return decorator


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)
