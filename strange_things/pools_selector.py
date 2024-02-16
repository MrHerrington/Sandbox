"""Программа определяет бассейн, который открыт в понедельник
в период с 10:00 до 12:00 с наиболее длинной дорожкой"""


import json
import datetime


with open('../testing_data/pools.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)
    address = ''
    length = 0
    width = 0
    for i in data:
        for k, v in dict(i['WorkingHoursSummer']).items():
            time = str(v).split('-')
            start = datetime.time(datetime.datetime.strptime(time[0], '%H:%M').hour,
                                  datetime.datetime.strptime(time[0], '%H:%M').minute)
            end = datetime.time(datetime.datetime.strptime(time[1], '%H:%M').hour,
                                datetime.datetime.strptime(time[1], '%H:%M').minute)
            if start <= datetime.time(10, 0) and end >= datetime.time(12, 0) \
                    and k == 'Понедельник':
                if i['DimensionsSummer']['Length'] >= length \
                        and i['DimensionsSummer']['Length'] * i['DimensionsSummer']['Width'] > length * width:
                    address = i['Address']
                    length = i['DimensionsSummer']['Length']
                    width = i['DimensionsSummer']['Width']
    print('{}x{}'.format(length, width))
    print('{}'.format(address))
