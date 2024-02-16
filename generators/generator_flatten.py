def flatten(nested_list):
    """Функция-генератор выполняет линеаризацию вложенных списков"""
    if isinstance(nested_list, int):
        yield nested_list
    if isinstance(nested_list, list):
        for lists in nested_list:
            yield from flatten(lists)


generator = flatten([[1, 2], [[3]], [[4], 5]])
print(*generator)


generator = flatten([1, 2, 3, 4, 5, 6, 7])
print(*generator)
