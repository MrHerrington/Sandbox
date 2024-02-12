import re


result = re.split(r'(?:\s*or\s*)|(?:\s*and\s*)|(?:\s*\|\s*)|(?:\s*&\s*)', str(input()))
print(*result, sep=', ')
