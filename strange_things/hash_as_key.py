def hash_as_key(_data):
    """
    Функция возвращает словарь, ключом в котором является хеш-значение объекта из
    списка, а значением — сам объект. Если хеш-значения некоторых объектов совпадают,
    они объединяются в список.
    """
    hash_dct = dict()

    for i in _data:
        if hash_dct.get(hash(i), 0) == 0:  # if not a pair key-value in dict
            hash_dct[hash(i)] = i
        elif type(hash_dct[hash(i)]) is list:  # if you need to add a new value in existing key
            hash_dct[hash(i)].append(i)
        elif type(hash_dct[hash(i)]) is int:  # if you have one value
            temp = hash_dct[hash(i)]  # create a temp value
            hash_dct[hash(i)] = list()  # create an empty list
            hash_dct[hash(i)].append(temp)  # adding the temp value
            hash_dct[hash(i)].append(i)  # adding the new value

    return hash_dct


data = [-1, -2, -3, -4, -5]
print(hash_as_key(data))
