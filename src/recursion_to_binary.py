def to_binary(num):
    """
    Функция переводит число из десятичной системы счисления в двоичную
    """
    if num <= 1:
        return str(num)
    else:
        s = '' + str(num % 2)
        return to_binary(num // 2) + s


print(to_binary(914646456))
