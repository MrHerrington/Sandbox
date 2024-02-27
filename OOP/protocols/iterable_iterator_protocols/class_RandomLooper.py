from random import shuffle


class RandomLooper:
    def __init__(self, *args):
        self._args = list()
        for i in args:
            self._args.extend(i)
        shuffle(self._args)
        self._index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self._args):
            raise StopIteration
        return self._args[self._index]


# Test №1
randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])
print(list(randomlooper))
print(list(randomlooper))

# Test №2
colors = ['red', 'blue', 'green', 'purple']
shapes = ['square', 'circle', 'triangle', 'octagon']
randomlooper = RandomLooper(colors, shapes)
print(list(randomlooper))
