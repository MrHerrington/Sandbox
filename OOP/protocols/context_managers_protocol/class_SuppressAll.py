class SuppressAll:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


print('start')

with SuppressAll():
    print('Press F Billy Herrington!')
    raise ValueError

print('end')
