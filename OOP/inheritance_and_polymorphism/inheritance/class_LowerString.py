class LowerString(str):
    def __new__(cls, obj):
        instance = ''
        if isinstance(obj, str) and not instance:
            instance = obj.lower()
        elif isinstance(obj, list):
            instance = [i.lower() for i in obj]
        elif isinstance(obj, dict):
            instance = {key.lower(): value for key, value in obj.items()}
        return instance


# Test №1
s1 = LowerString('DUNGEON')
s2 = LowerString('DunGeon')

print(s1)
print(s2)
print(s1 == s2)
print(issubclass(LowerString, str))

# Test №2
print(LowerString(['Dun', 'Geon']))
print(LowerString({'A': 1, 'B': 2, 'C': 3}))

# Test №3
s = LowerString('DunGeon')
print(s[0], s[3])
