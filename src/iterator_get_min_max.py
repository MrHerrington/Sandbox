def get_min_max(_data):
    """Функция возвращает кортеж, в котором первым элементом является индекс
    минимального элемента в списке, вторым — индекс максимального элемента в
    списке. Если список пуст, функция вернет значение None.
    Или возвращает кортеж, в котором первым элементом является минимальный
    элемент итерируемого объекта, вторым — максимальный элемент итерируемого
    объекта. Если итерируемый объект пуст, функция вернет значение None."""
    result = []
    if type(_data) in (str, tuple, list):
        for i, j in enumerate(_data):
            if j == min(_data):
                if _data.index(j) not in result:
                    result.append(i)
        for i, j in enumerate(_data):
            if j == max(_data):
                result.append(i)
                break
    else:
        minimum = 10 ** 6
        maximum = -10 * 10 ** 5
        while True:
            try:
                temp = next(_data)
                if temp < minimum:
                    minimum = temp
                if temp > maximum:
                    maximum = temp
            except StopIteration:
                if minimum != 10 ** 6:
                    result.append(minimum)
                if maximum != -10 * 10 ** 5:
                    result.append(maximum)
                break
    if bool(result) is True:
        return tuple(result)
    else:
        return None


data = [2, 3, 8, 1, 7]
print(get_min_max(data))


data = [1, 1, 2, 3, 8, 8]
print(get_min_max(data))


data = [9]
print(get_min_max(data))


iterable = iter(range(10))
print(get_min_max(iterable))


iterable = [6, 4, 2, 33, 19, 1]
print(get_min_max(iterable))


iterable = iter([])
print(get_min_max(iterable))
