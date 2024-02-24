from datetime import date


class DateFormatter:
    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d):
        locals_dict = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d',
                       'br': '%d/%m/%Y', 'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y'}
        return date.strftime(d, locals_dict[self.country_code])


# Test №1
ru_format = DateFormatter('ru')

print(ru_format(date(2022, 11, 7)))

# Test №2
us_format = DateFormatter('us')

print(us_format(date(2022, 11, 7)))

# Test №3
ca_format = DateFormatter('ca')

print(ca_format(date(2022, 11, 7)))
