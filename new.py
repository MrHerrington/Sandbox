def likes(lst):
    if len(lst) == 0:
        return 'Никто не оценил данную запись'
    elif len(lst) == 1:
        return f'{lst[0]} оценил(а) данную запись'
    elif len(lst) == 2:
        return f'{lst[0]} и {lst[1]} оценили данную запись'
    elif len(lst) == 3:
        return f'{lst[0]}, {lst[1]} и {lst[2]} оценили данную запись'
    else:
        return f'{lst[0]}, {lst[1]} и {len(lst) - 2} других оценили данную запись'


print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))

# sfafaf
