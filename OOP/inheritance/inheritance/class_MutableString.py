from collections import UserString


class MutableString(UserString):
    def __setitem__(self, index, value):
        data_as_list = list(self.data)
        data_as_list[index] = value
        self.data = "".join(data_as_list)

    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        self.data = "".join(sorted(self.data, key=key, reverse=reverse))


# Test №1
mutablestring = MutableString('Dungeon')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
mutablestring.sort()
print(mutablestring)

# Test №2
mutablestring = MutableString('dungeon')

print(mutablestring)
mutablestring[0] = 'D'
mutablestring[-4] = 'G'
print(mutablestring)
