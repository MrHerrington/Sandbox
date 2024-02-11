import re


def abbreviate(text):
    result = re.finditer(r'(\b\w)|[A-Z]', text)
    return ''.join(map(lambda x: x.group().upper(), result))


print(abbreviate('javaScript object notation'))
print(abbreviate('frequently asked questions'))
print(abbreviate('JS game sec'))