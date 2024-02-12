"""Программа заменяет все повторяющиеся рядом стоящие слова на одно слово:
hi, hi, hi, hello, hello, HELLO, HELLO, HELLO, HELLO, hello! -> hi, hello, HELLO, hello!"""


import re


request = str(input())
word_list = re.findall(r'\w+\W*', request)
temp_word = ''
result_list = list()
for word in word_list:
    if not temp_word:
        temp_word = word.strip()
        continue
    if re.search(r'\w+', word).group() in temp_word:
        temp_word = word.strip()
        continue
    else:
        result_list.append(temp_word)
        temp_word = word.strip()
result_list.append(temp_word)
print(*result_list)
