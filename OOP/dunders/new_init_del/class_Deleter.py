from sys import getrefcount


class Deleter:
    def __del__(self):
        print('Object deleted!')


obj = Deleter()
print(getrefcount(obj))
del obj
print(getrefcount(obj))
