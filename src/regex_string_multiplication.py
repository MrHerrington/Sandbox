"""Программа, которая раскрывает все умножения в тексте и выводит полученный результат:
hi2(priv3(d3(i)dd)qq)b0(pr)qwqdd ->
hiprivdiiidddiiidddiiiddqqprivdiiidddiiidddiiiddqqbqwqdd"""


import re


def string_multiplication(_obj):
    temp = _obj.group()
    multiplicator = int(re.search(r'\d+', temp).group())
    text_string = re.search(r'[A-Za-z]+', temp).group()
    return multiplicator * text_string


request = str(input())
while re.search(r'\(\w+\)', request):
    request = re.sub(r'\d+\(\w+\)', string_multiplication, request)
print(request)
