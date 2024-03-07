class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if value == v:
                return k

    def keys_of(self, value):
        for k, v in self.items():
            if value == v:
                yield k


# Test №1
valuedict = ValueDict({'apple': 1, 'banana': 2, 'orange': 2})

print(valuedict.key_of(2))
print(*valuedict.keys_of(2))

# Test №2
valuedict = ValueDict({})

print(valuedict.key_of(12))
print(*valuedict.keys_of(33))
