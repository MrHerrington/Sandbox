"""
Программа, используя рекурсию, принимает на вход число и вычитает из него число 5,
пока оно не перестанет быть положительным, а затем прибавляет к нему число, пока оно
снова не станет равным начальному значению.
"""


def no_cycles(n):
    flag = True

    def no_cycles_rec(m, check):
        if m <= 0:
            check = False
        if check:
            print(m)
            return no_cycles_rec(m - 5, check)
        elif not check and m <= n:
            print(m)
            return no_cycles_rec(m + 5, check)

    return no_cycles_rec(n, flag)


no_cycles(101)
