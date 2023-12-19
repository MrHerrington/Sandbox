n, m = [int(i) for i in input().split()]
matrix1 = [list(int(i) for i in input().split()) for _ in range(n)]
s_empty = input()
m, k = [int(i) for i in input().split()]
matrix2 = [list(int(i) for i in input().split()) for _ in range(m)]
matrix3 = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for p in range(m):
            matrix3[i][j] += matrix1[i][p] * matrix2[p][j]
for i in matrix3:
    print(*i)
