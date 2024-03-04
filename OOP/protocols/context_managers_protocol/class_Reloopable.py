class Reloopable:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return tuple(self.obj.read().splitlines())

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.obj.close()


with open(r'C:\Users\user\PycharmProjects\Sandbox\testing_data\reloopable.txt', 'w') as file:
    file.write('Evil is evil\n')
    file.write('Lesser, greater, middling\n')
    file.write('Makes no difference\n')

with Reloopable(open(r'C:\Users\user\PycharmProjects\Sandbox\testing_data\reloopable.txt')) as reloopable:
    for line in reloopable:
        print(line.strip())
    for line in reloopable:
        print(line.strip())
