"""Программа, складывает все натуральные числа в строке,
находящиеся в указанном диапазоне индексов."""


import re


indexes = list(map(int, str.split(input())))
text = str(input())
regex_obj = re.compile(r'\d+')
result = list(map(int, regex_obj.findall(text, pos=indexes[0], endpos=indexes[-1])))
if result:
    print(sum(result))
else:
    print('Нет ни одного числа в этой строке')
