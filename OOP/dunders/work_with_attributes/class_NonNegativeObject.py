class NonNegativeObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if type(v) in (int, float):
                object.__setattr__(self, k, abs(v))
            else:
                object.__setattr__(self, k, v)

    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)


# Test №1
point = NonNegativeObject(x=1, y=-2, z=0, color='black')

print(point.x)
print(point.y)
print(point.z)
print(point.color)

# Test №2
point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')
print(point.x)
print(point.y)
print(point.z)
print(point.color)
