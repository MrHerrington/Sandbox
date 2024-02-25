class AttrsNumberObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __getattribute__(self, attr):
        if attr == 'attrs_num':
            return len(object.__getattribute__(self, '__dict__')) + 1
        else:
            return object.__getattribute__(self, attr)


# Test №2
music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

print(music_group.attrs_num)

# Test №2
music_group = AttrsNumberObject()

print(music_group.attrs_num)

# Test №3
music_group = AttrsNumberObject(name='Woodkid', genre='pop')
print(music_group.attrs_num)

music_group.country = 'France'
print(music_group.attrs_num)

# Test №4
music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)
