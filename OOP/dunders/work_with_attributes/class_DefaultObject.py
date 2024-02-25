class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __getattribute__(self, attr):
        try:
            if object.__getattribute__(self, attr):
                return object.__getattribute__(self, attr)
        except AttributeError:
            return object.__getattribute__(self, 'default')


# Test №1
god = DefaultObject(name='Ares', mythology='greek')
print(god.__dict__)
print(god.name)
print(god.mythology)
print(god.age)

# Test №2
god = DefaultObject(default=0, name='Tyr', mythology='scandinavian')

print(god.name)
print(god.mythology)
print(god.age)
