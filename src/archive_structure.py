"""
Программа выводит файловую структуру заданного архива и объем каждого файла в
несжатом виде. Так как архив имеет собственную иерархию папок, каждый уровень
вложенности выделяется двумя пробелами.
"""


from zipfile import ZipFile


def size_conv(size):    # Функция конвертации размера файлов в удобном человеку виде
    if size < 1024:
        return size, 'B'
    elif 1024 <= size < 1048576:
        return round(size / 1024), 'KB'
    elif 1048576 <= size < 1073741824:
        return round(size / 1048576), 'MB'
    elif size >= 1073741824:
        return round(size / 1073741824), 'GB'


with ZipFile('../config/test.zip', 'r') as zip_file:
    dct = {}    # Словарь вида {полный путь файла - путь в виде списка}
    for i in zip_file.namelist():
        tmp = zip_file.getinfo(i).filename.split('/')
        while '' in tmp:    # Удаляем лишние пустые позиции в списке значений словаря
            tmp.remove('')
        dct[i] = tmp
    for k, v in sorted(dct.items(), key=lambda x: [str(j).lower() for j in x[1]]):  # Сортировка по значениям словаря
        if zip_file.getinfo(k).file_size == 0:
            print(f'{"  " * v.index(v[-1])}{v[-1]}')    # Размер для папок не выводится
        else:
            print(f'{"  " * v.index(v[-1])}{v[-1]}', end=' ')   # Выводятся отступы, имя файла и значение размера из
            # кортежа функции
            print(*size_conv(zip_file.getinfo(k).file_size))    # Выводятся единицы измерения размера файла из
            # кортежа функции
