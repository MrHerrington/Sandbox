def is_power(n):
    """
    Функция возвращает значение True, если number является
    степенью числа 2, или False в противном случае.
    """
    try:
        if n == 1:
            return True
        else:
            return is_power(n / 2)
    except RecursionError:
        return False


print(is_power(258))
