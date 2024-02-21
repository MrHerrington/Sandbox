class AnyClass:
    def __init__(self, **kwargs):
        self._arguments = list(f'{key}={repr(value)}' for key, value in kwargs.items())

    def __str__(self):
        return f"AnyClass: {', '.join(self._arguments)}"

    def __repr__(self):
        return f"AnyClass({', '.join(self._arguments)})"


any_ = AnyClass()
print(str(any_))
print(repr(any_))

cowboy = AnyClass(name='John', surname='Marston')
print(str(cowboy))
print(repr(cowboy))

obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3],
               attr5=('one', 'two'), attr6=None)
print(str(obj))
print(repr(obj))
print(eval(repr(obj)))
