def recursive_sum(nested_lists):
    """
    Функция определяет сумму значений всех вложенных списков
    """
    total = 0

    def recursive_sum_rec(lst):
        nonlocal total
        if type(lst) is int:
            total += lst
        if type(lst) is list:
            for i in lst:
                recursive_sum_rec(i)
        return total

    return recursive_sum_rec(nested_lists)


my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))
