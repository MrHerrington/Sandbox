"""На вход программе на первой строке подается слово, которое записано в Британском варианте,
а на следующей — текст. Программа определяет, сколько раз слово встречается в тексте, учитывая
его Британско-Американское написание."""


import re


pattern_request = str(input())
text = str(input())
result = re.finditer(r"\b%s(ou|o)%s\b" % (pattern_request[:pattern_request.find('ou')],
                                          pattern_request[pattern_request.rfind('ou') + 2:]),
                     text, re.IGNORECASE)
print(sum(map(bool, result)))
