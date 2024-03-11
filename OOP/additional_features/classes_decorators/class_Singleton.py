class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __call__(self, *args, **kwargs):
        return self


@Singleton
class MyClass:
    pass


obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2)
