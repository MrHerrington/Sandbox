from collections import namedtuple
import itertools

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

weight = int(input())
total_price = 0
best_comb = 'Рюкзак собрать не удастся'

try:
    for i in range(1, len(items)):
        comb = itertools.combinations(items, i)
        for j in comb:
            if sum(map(lambda x: x.mass, j)) <= weight and sum(map(lambda x: x.price, j)) >= total_price:
                total_price = sum(map(lambda x: x.price, j))
                best_comb = j
    print(*sorted(map(lambda x: x.name, best_comb)), sep='\n')
except AttributeError:
    print(best_comb)
