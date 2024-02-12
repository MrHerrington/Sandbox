from re import sub
from keyword import iskeyword


def _is_keyword(_obj):
    """Функция заменяет ключевые слова на <kw>"""
    temp = _obj.group()
    if iskeyword(temp.lower()) or iskeyword(temp.capitalize()):
        return '<kw>'
    else:
        return temp


request = str(input())
print(sub(r'\w+', _is_keyword, request))
