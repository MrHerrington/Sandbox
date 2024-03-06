class FieldTracker:
    def __init__(self):
        self._values = {field: getattr(self, field)
                        for field in self.fields}

    def base(self, field):
        return self._values[field]

    def has_changed(self, field):
        return self._values[field] != getattr(self, field)

    def changed(self):
        return {field: self.base(field)
                for field in self.fields
                if self.has_changed(field)}

    def save(self):
        for field in self.fields:
            self._values[field] = getattr(self, field)


# Test №1
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


point = Point(1, 2, 3)

print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())


# Test №2
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.z = 5

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())


# Test №3
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.save()

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())
