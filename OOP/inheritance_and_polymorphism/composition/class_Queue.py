class Queue:
    def __init__(self, pairs=None):
        if pairs is None:
            self.pairs = list()
        else:
            if type(pairs) is dict:
                self.pairs = list(zip(pairs.keys(), pairs.values()))
            else:
                self.pairs = pairs

    def __len__(self):
        return len(self.pairs)

    def add(self, new):
        for key in self.pairs:
            if new[0] == key[0]:
                self.pairs.remove(key)
        self.pairs.append(new)

    def pop(self):
        if not self.pairs:
            raise KeyError('Очередь пуста')
        return self.pairs.pop(0)

    def __repr__(self):
        return f'Queue({self.pairs})'


# Test №1
queue = Queue()

queue.add(('one', 1))
queue.add(('two', 2))
print(queue)

# Test №2
queue = Queue([('one', 1)])

queue.add(('two', 2))
print(queue.pop())
print(queue.pop())
print(queue)

# Test №3
queue = Queue({'one': 1, 'two': 2})

print(len(queue))
queue.add(('three', 1))
print(len(queue))

# Test №4
queue = Queue()

queue.add(('one', 1))
queue.add(('two', 2))
print(queue)
queue.add(('one', 10))
print(queue)

# Test №5
queue = Queue()

try:
    queue.pop()
except KeyError as error:
    print(error)
