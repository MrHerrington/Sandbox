import re


text = str(input())
search_querry = re.search(r'(?P<country_code>\d+)([ -]?)(?P<city_code>\d+)\2(?P<number>\d+)', text)
print(f"Код страны: {search_querry.group('country_code')}")
print(f"Код города: {search_querry.group('city_code')}")
print(f"Номер: {search_querry.group('number')}")
