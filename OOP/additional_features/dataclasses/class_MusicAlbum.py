from dataclasses import dataclass, field


@dataclass(frozen=True)
class MusicAlbum:
    title: str
    artist: str
    genre: str = field(compare=False)
    year: int


# Test №1
print(MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012))

# Test №2
musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
musicalbum2 = MusicAlbum('Calendar', 'Motorama', 'New Wave, Indie Rock', 2012)

print(musicalbum1 == musicalbum2)
print(musicalbum1 != musicalbum2)

# Test №3
musicalbum = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)

try:
    musicalbum.genre = 'Post-punk, New Wave, Indie Rock'
except:
    print('Error')
