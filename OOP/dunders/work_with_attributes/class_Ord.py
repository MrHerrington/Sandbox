class Ord:
    def __getattr__(self, attr):
        return ord(attr)


# Test №1
obj = Ord()
print(obj.a)
print(obj.b)

# Test #2
obj = Ord()

print(obj.в)
print(obj.г)
