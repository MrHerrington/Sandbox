def linear(nested_lists):
    """
    Функция выполняет линеаризацию вложенных списков
    """
    result = []

    def recursive_sum_rec(lst):
        nonlocal result
        if type(lst) is int:
            result.append(lst)
        if type(lst) is list:
            for i in lst:
                recursive_sum_rec(i)
        return result

    return recursive_sum_rec(nested_lists)


my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(linear(my_list))
