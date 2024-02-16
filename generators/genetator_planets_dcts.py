with open('../testing_data/planets.txt', 'r', encoding='UTF-8') as file:
    datas = (planet.split('\n')
             for planet in file.read().split('\n\n'))
    dct = ({j.split('=')[0]: str(j.split('=')[-1]).strip() for j in i} for i in datas)
    for i in dct:
        print(i)
