class DictItems:
    def __init__(self, _data):
        self.data = _data
        self.index = -1
        self.lst = list(_data)

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.data):
            raise StopIteration
        return tuple((self.lst[self.index], self.data[self.lst[self.index]]))


data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
pairs = DictItems(data)
print(*pairs)
