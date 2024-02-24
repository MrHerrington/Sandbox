class SortKey:
    def __init__(self, *args):
        self.args = args

    def __call__(self, obj):
        attr_lst = list()
        for i in self.args:
            attr_lst.append(getattr(obj, i))
        return attr_lst


# Test №1
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20),
         User('Timur', 45), User('Gvido', 60)]

print(sorted(users, key=SortKey('name')))
print(sorted(users, key=SortKey('name', 'age')))
print(sorted(users, key=SortKey('age')))
print(sorted(users, key=SortKey('age', 'name')))


# Test №2
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20),
         User('Timur', 45), User('Gvido', 60)]

print(max(users, key=SortKey('name')))
print(max(users, key=SortKey('age')))
print(max(users, key=SortKey('name', 'age')))
print(max(users, key=SortKey('age', 'name')))
