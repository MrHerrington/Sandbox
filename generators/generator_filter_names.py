def filter_names(_data, ignore_char, count):
    filtered_data = (i for i in _data
                     if i[0].lower() != ignore_char.lower() and all(map(lambda x: x.isalpha(), i)))
    counter = 0
    try:
        while counter != count:
            yield next(filtered_data)
            counter += 1
    except StopIteration:
        pass


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 't', 20))
