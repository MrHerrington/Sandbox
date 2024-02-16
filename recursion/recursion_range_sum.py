def range_sum(_numbers, _start, _end):
    """
    Функция суммирует все числа из списка numbers
    от numbers[start] до numbers[end] включительно
    и возвращает полученный результат
    """
    i = _start

    def range_sum_rec():
        if i == _end:
            return _numbers[i]
        else:
            return _numbers[i] + range_sum(_numbers, i + 1, _end)

    return range_sum_rec()


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
