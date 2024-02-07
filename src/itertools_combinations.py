from itertools import combinations


wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
excpt = set()
for i in range(1, len(wallet)):
    comb = combinations(wallet, i)
    for j in comb:
        if sum(j) == 100 and j not in excpt:
            excpt.add(j)
            print(f'{i} способ: ', end='')
            print(*j, sep=', ')
