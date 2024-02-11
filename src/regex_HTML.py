"""Программа находит во фрагменте HTML-страницы все гиперссылки
и выводит их составляющие — адресные части и указатели."""


import re
import sys


text = sys.stdin.read()
hyper_links = re.findall(r'<a href=.+/a>', text, re.MULTILINE)
for link in hyper_links:
    address = re.search(r'\"(.+)\"', link)
    name = lambda x: name(re.search(r'>(.+)<', x).group(1)) if '>' in x else x
    print(address.group(1), name(link), sep=', ')
