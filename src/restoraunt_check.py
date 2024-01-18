"""
Программа принимает на вход ингредиенты, выбранные посетителем заведения, и определяет
их общую стоимость. На вход программе подается последовательность ингредиентов, разделенных
запятой без пробелов. Программа выводит результат в виде чека: продукты и их количество
в лексикографическом порядке, пунктирная линия, итоговая строка с общей суммой.
"""


from collections import ChainMap, Counter
import sys


bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

product_prices = ChainMap(bread, meat, sauce, vegetables, toppings)

request = [i for i in sys.stdin.read().strip().split(',')]
request_quantities = Counter(request)

# len longest product position and total line
len_longest_product = (max(map(len, request_quantities.keys())) + 3 +
                       max(map(lambda x: len(str(x)), request_quantities.values())))
total_line = f"ИТОГ: {sum([product_prices[k] * v for k, v in request_quantities.items()])}"
len_total_line = len(total_line)

# Show product position and price
for k, v in sorted(request_quantities.items()):
    print(f"{k}{' ' * (max(map(len, request_quantities.keys())) - len(k))} x {v}")
print(max((len_longest_product, len_total_line)) * '-')
print(total_line)
