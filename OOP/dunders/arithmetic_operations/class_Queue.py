class Queue:
    """Класс описывает очередь"""
    def __init__(self, *args):
        self.args = list(args)

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.args == other.args
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*(self.args + other.args))
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.args += other.args
            return self
        else:
            return NotImplemented

    def __rshift__(self, other):
        return Queue(*(self.args[other:]))

    def __str__(self):
        return ' -> '.join(map(str, self.args))

    def add(self, *args):
        self.args.extend(args)

    def pop(self):
        try:
            return self.args.pop(0)
        except IndexError:
            return None


# Test №1
queue = Queue(1, 2)

queue.add(3)
queue.add(4, 5)

print(queue)
print(queue.pop())
print(queue)

# Test №2
queue1 = Queue(1, 2, 3)
queue2 = Queue(1, 2)

print(queue1 == queue2)
queue2.add(3)
print(queue1 == queue2)

# Test №3
queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

print(queue1 + queue2)

# Test №4
queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

queue1 += queue2

print(queue1)

# Test №5
queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)
