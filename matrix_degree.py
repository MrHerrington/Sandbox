import copy
n = int(input())
matrix1 = [list(int(i) for i in input().split()) for _ in range(n)]
m = int(input())
matrix2 = copy.deepcopy(matrix1)
matrix3 = [list(0 for i in range(n)) for _ in range(n)]
for c in range(m - 1):
    matrix3 = [list(0 for i in range(n)) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for p in range(n):
                matrix3[i][j] += matrix1[i][p] * matrix2[p][j]
    matrix1 = copy.deepcopy(matrix3)
for i in matrix3:
    print(*i)
