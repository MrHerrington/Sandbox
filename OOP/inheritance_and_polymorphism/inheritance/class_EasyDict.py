from collections import UserDict


class EasyDict(UserDict):
    def __getattr__(self, item):
        return self.data[item]


# Test №1
easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

print(easydict['name'])
print(easydict.city)

# Test №2
easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

easydict['city'] = 'Dubai'
easydict['age'] = 30

print(easydict.city)
print(easydict.age)

# Test №3
easydict = EasyDict({'name': 'Artur', 'city': 'Almetevsk'})

easydict.age = 21
print(easydict)
