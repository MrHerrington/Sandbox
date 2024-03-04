import os.path
from tempfile import TemporaryFile
from pympler import asizeof


class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.obj.close()
        except AttributeError:
            print('Незакрываемый объект')


# Test №1
with Closer(TemporaryFile()) as file:
    file.write(b'Gym')
    print(asizeof.asizeof(file))
    print(file.closed)

print(file.closed)


# Test №2
with Closer(5) as i:
    i += 1

print(i)
