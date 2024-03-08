from datetime import date


class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return date(self.year, self.month, self.day).strftime('%m-%d-%Y')

    def iso_format(self):
        return date(self.year, self.month, self.day)


class ItalianDate(USADate):
    def format(self):
        return date(self.year, self.month, self.day).strftime('%d/%m/%Y')


# Test №1
usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())

# Test №2
italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())
