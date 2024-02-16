def get_fast_pow(a, n):
    """
    Быстрое возвдение в степень реализовано с помощью рекуррентных соотношений:
    a^n = (a^2)^(n/2), при четном n
    a^n = a * a^(n - 1), при нечетном n
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return get_fast_pow(a * a, n / 2)
    else:
        return a * get_fast_pow(a, n - 1)


print(get_fast_pow(5, 4))
