from enum import Flag


class MovieGenres(Flag):
    ACTION = 1
    COMEDY = 2
    DRAMA = 4
    FANTASY = 8
    HORROR = 16


class Movie:
    def __init__(self, name, genres):
        self.name = name
        self.genres = genres

    def __str__(self):
        return f'{self.name}'

    def in_genre(self, genre):
        return genre in self.genres


# Test №1
movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)

print(movie)

# Test №2
movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)
print(movie.in_genre(MovieGenres.FANTASY))
print(movie.in_genre(MovieGenres.COMEDY))
print(movie.in_genre(MovieGenres.ACTION | MovieGenres.FANTASY))
