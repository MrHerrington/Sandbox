class AdvancedList(list):
    def join(self, sep=' '):
        return sep.join(map(str, self))

    def map(self, func):
        for i in range(len(self)):
            self[i] = func(self[i])

    def filter(self, func):
        for i in range(len(self)):
            if not func(self[i]):
                self[i] = None
        while None in self:
            self.remove(None)


# Test №1
advancedlist = AdvancedList([1, 2, 3, 4, 5])
print(advancedlist.join())
print(advancedlist.join('-'))

# Test №2
advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.map(lambda x: -x)

print(advancedlist)

# Test №3
advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.filter(lambda x: x % 2 == 0)

print(advancedlist)

# Test №4
advancedlist = AdvancedList([0, 1, 2, '', 3, (), 4, 5, False, {}])
id1 = id(advancedlist)

advancedlist.filter(bool)
id2 = id(advancedlist)

print(advancedlist)
print(id1 == id2)
