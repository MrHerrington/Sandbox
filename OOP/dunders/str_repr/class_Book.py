class Book:
    """Класс описывает книгу"""
    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year

    def __str__(self):
        return f'{self._title} ({self._author}, {self._year})'

    def __repr__(self):
        return f"Book('{self._title}', '{self._author}', '{self._year}')"


book = Book('Изучаем Python', 'Марк Лутц', 2021)
print(book)
print(repr(book))
print(eval(repr(book)))
