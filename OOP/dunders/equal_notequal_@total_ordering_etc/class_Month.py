from functools import total_ordering
from datetime import date


@total_ordering
class Month:
    """Класс описывает месяц"""
    def __init__(self, year, month):
        self._year = year
        self._month = month

    def __eq__(self, other):
        """self == other"""
        if isinstance(other, Month):
            return date(self.year, self.month, 1) == date(other.year, other.month, 1)
        else:
            return NotImplemented

    def __lt__(self, other):
        """self < other"""
        if isinstance(other, Month):
            return date(self.year, self.month, 1) < date(other.year, other.month, 1)
        else:
            return NotImplemented

    def __str__(self):
        return f'{self.year}-{self.month}'

    def __repr__(self):
        return f'Month({self.year}, {self.month})'

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month


# Test №1
print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))

# Test №2
months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]
print(sorted(months))

# Test №3
months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]
print(min(months))
print(max(months))
