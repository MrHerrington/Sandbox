"""Программа показывает самого молодого человека с ДР в ближайшие 7 дней """


from datetime import datetime, timedelta


dct = {}
s = datetime.strptime(input(), '%d.%m.%Y')  # Дата формата "ДД.ММ.ГГГГ"
n = int(input())  # Количество человек
for i in range(n):
    d = input().split()  # Ввод информации вида "Имя Фамилия ДД.ММ.ГГГГ"
    dct[' '.join(d[:2])] = datetime.strptime(d[2], '%d.%m.%Y')
lst = []
for i in range(7):
    s = s + timedelta(days=1)
    lst.append(s)
res = []
for k, v in dct.items():
    for i in lst:
        if (dct[k].day, dct[k].month) == (i.day, i.month):
            res.append(k)
if res:
    print(max(res, key=lambda x: dct[x]))
else:
    print('Дни рождения не планируются')
