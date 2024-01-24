def get_all_values(nested_dicts, key):
    """
    Функция возвращает множество значений по ключу среди всех вложенных словарей
    """
    vals = set()

    def get_all_values_rec(_nested_dicts, _key):
        if _key in _nested_dicts:
            return _nested_dicts[_key]

        for keys, values in _nested_dicts.items():
            if type(values) is dict:
                value = get_all_values_rec(values, _key)
                if value is not None:
                    vals.add(value)

    get_all_values_rec(nested_dicts, key)
    return vals


my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))
