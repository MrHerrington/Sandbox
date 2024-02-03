import csv


with open('../config/investitions.csv', 'r', encoding='UTF-8') as file:
    datas = csv.reader(file, delimiter=',', lineterminator='\n')
    header = next(datas)
    positions = (i for i in datas if i[-1] == 'a')
    print(sum(int(j[1]) for j in positions))
