from functools import total_ordering


@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral.to_arabic(self.number) == RomanNumeral.to_arabic(other.number)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral.to_arabic(self.number) < RomanNumeral.to_arabic(other.number)
        else:
            return NotImplemented

    def __int__(self):
        return RomanNumeral.to_arabic(self.number)

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(RomanNumeral.to_roman(
                RomanNumeral.to_arabic(self.number) + RomanNumeral.to_arabic(other.number)))
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(RomanNumeral.to_roman(
                RomanNumeral.to_arabic(self.number) - RomanNumeral.to_arabic(other.number)))
        else:
            return NotImplemented

    def __str__(self):
        return f'{self.number}'

    @staticmethod
    def to_arabic(roman_num):
        roman_numbers = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4,
                         'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        def _():
            nonlocal roman_num
            arabic_num = 0
            while roman_num != "":
                for letter, value in roman_numbers.items():
                    if letter in roman_num:
                        arabic_num += value
                        roman_num = roman_num.replace(letter, "", 1)
            return arabic_num
        return _()

    @staticmethod
    def to_roman(arabic_num):
        roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                         'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        def _():
            nonlocal arabic_num
            roman = ''
            for letter, value in roman_numbers.items():
                while arabic_num >= value:
                    roman += letter
                    arabic_num -= value
            return roman
        return _()


# Test №1
number = RomanNumeral('IV') + RomanNumeral('VIII')

print(number)
print(int(number))

# Test №2
number = RomanNumeral('X') - RomanNumeral('VI')

print(number)
print(int(number))

# Test №3
a = RomanNumeral('X')
b = RomanNumeral('XII')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
