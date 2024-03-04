class ReadableTextFile:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        self.obj = open(self.obj, 'r', encoding='utf-8')
        yield from self.obj.read().splitlines()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.obj.close()


with open(r'C:\Users\user\PycharmProjects\Sandbox\testing_data\glados_quotes.txt', 'w', encoding='utf-8') as file:
    print('Только посмотрите!', file=file)
    print('Как величаво она парит в воздухе', file=file)
    print('Как орел', file=file)
    print('На воздушном шаре', file=file)

with ReadableTextFile(r'C:\Users\user\PycharmProjects\Sandbox\testing_data\glados_quotes.txt') as file:
    for line in file:
        print(line)
