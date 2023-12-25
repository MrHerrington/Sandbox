"""Модификация калькулятора систем счисления, позволяет с помощью функции определить в какой системе счисления
посчитано определенное количество предметов"""


def scale_calc(n, base):
    dict_16 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    number = 0
    for i in range(len(str(n))):
        if str(n)[i].isdigit():
            number += int(str(n)[i]) * base ** (len(str(n)) - 1 - i)
        elif str(n)[i] in 'ABCDEF':
            number += dict_16[str(n)[i]] * base ** (len(str(n)) - 1 - i)
    return number


for a in range(16):
    if (scale_calc(32, a) + scale_calc(22, a) + scale_calc(16, a) + scale_calc(17, a)) == \
            scale_calc(88, a):
        print(a)
