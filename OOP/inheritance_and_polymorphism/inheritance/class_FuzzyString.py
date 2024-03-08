class FuzzyString(str):
    def __eq__(self, other):
        if isinstance(other, FuzzyString):
            return self.lower() == other.lower()
        else:
            return NotImplemented

    def __contains__(self, item):
        if isinstance(item, FuzzyString):
            return self.lower() in item.lower()
        else:
            return NotImplemented


s1 = FuzzyString('DunGeon')
s2 = FuzzyString('dungeon')
print(s1 == s2)
print(s1 in s2)
print(s2 in s1)
print(s2 not in s1)
print(s2 not in s1)
