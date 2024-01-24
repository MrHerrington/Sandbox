def dict_travel(nested_dicts):
    """
    Функция выводит все пары ключ-значение словаря,
    а также значения всех его дочерних словарей
    """
    result = dict()
    key = ''

    def dict_travel_rec(_nested_dicts):
        nonlocal key

        for no_dict_keys, no_dict_vals in _nested_dicts.items():
            if type(no_dict_vals) is not dict:
                if key:
                    result[key + no_dict_keys] = no_dict_vals
                else:
                    result[no_dict_keys] = no_dict_vals

        for dict_keys, dict_values in _nested_dicts.items():
            if type(dict_values) is dict:
                key = key + dict_keys + '.'
                dict_travel_rec(dict_values)

    dict_travel_rec(nested_dicts)
    for keys, values in sorted(result.items()):
        print(f'{keys}: {values}')


data = {'firstname': 'Тимур', 'lastname': 'Гуев',
        'birthdate': {'day': 10, 'month': 'October', 'year': 1993},
        'address': {'streetaddress': 'Часовая 25, кв. 127',
                    'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'},
                    'postalcode': '125315'}}

dict_travel(data)
