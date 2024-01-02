import json


with open('../config/food_services.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)
    types = set()
    for i in data:
        types.add(i['TypeObject'])
    result = {i: ['', 0] for i in types}
    for i in data:
        for k, v in result.items():
            if i['TypeObject'] == k and i['SeatsCount'] > v[1]:
                v[0], v[1] = i['Name'], i['SeatsCount']
    for i in sorted(result):
        print(f'{i}:{result[i][0]}, {result[i][1]}')
