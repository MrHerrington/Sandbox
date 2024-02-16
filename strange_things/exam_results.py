"""
Каждый студент имеет право пересдать экзамен два раза, поэтому он может встречаться в
исходном файле до трёх раз с различной оценкой и различными датой и временем сдачи.
Программа для каждого студента определяет его максимальную оценку, а также дату и
время ее получения.  Словари в списке расположены в лексикографическом порядке названий
электронных почт.
"""


import json
import datetime as dt


def check(oper, elem, massive):
    return lambda x: oper(x[elem]) == max(map(lambda y: oper(y[elem]), massive))


with open('../testing_data/exam_results.csv', 'r', encoding='UTF-8') as file1, \
        open('../testing_data/best_scores.json', 'w', encoding='UTF-8') as file2:
    data = [str(i).split(',') for i in file1.read().splitlines()]  # Извлечение данных
    data.pop(0)
    filtration = set()  # Множество исключений
    in_json = []
    for i in data:
        if tuple(i) in filtration:
            continue
        temp = [i]
        for j in data:
            if j[0] == i[0] and j[1] == i[1] and j[-1] == i[-1] and i != j:
                temp.append(j)
        for k in temp:
            filtration.add(tuple(k))
        res = list(*filter(check(int, 2, temp) and check(dt.datetime.fromisoformat, 3, temp), temp))
        temp_json = {'name': res[0],
                     'surname': res[1],
                     'best_score': int(res[2]),
                     'date_and_time': res[-2],
                     'email': res[-1]}
        in_json.append(temp_json)
    json.dump(sorted(in_json, key=lambda x: x['email']), file2, indent=3)
