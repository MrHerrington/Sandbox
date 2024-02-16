"""Показывает оставшееся время работы в мин. до закрытия магазина"""


from datetime import datetime


dct = {1: '9:00 - 21:00',
       2: '9:00 - 21:00',
       3: '9:00 - 21:00',
       4: '9:00 - 21:00',
       5: '9:00 - 21:00',
       6: '10:00 - 18:00',
       7: '10:00 - 18:00'}

s = input('Введите "ДД.ММ.ГГГГ HH:ММ": ').split()
dt = datetime.strptime(s[0], '%d.%m.%Y')
tm = datetime.strptime(s[1], '%H:%M')
for k, v in dct.items():
    dct[k] = (datetime.strptime(v.split(' - ')[0], '%H:%M'),
              datetime.strptime(v.split(' - ')[1], '%H:%M'))
if dct[dt.isoweekday()][0] <= tm < dct[dt.isoweekday()][1]:
    res = (dct[dt.isoweekday()][1] - tm).seconds / 60
    print(res)
else:
    print('Магазин не работает')
