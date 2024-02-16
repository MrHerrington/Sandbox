s = [int(i) for i in str(input()).split()]
n, m = s[0], s[1]
matrix1 = [list(int(i) for i in str(input()).split()) for _ in range(n)]
s_empty = input()
matrix2 = [list(int(i) for i in str(input()).split()) for _ in range(n)]
matrix3 = [list(int(0) for i in range(m)) for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
        print(matrix3[i][j], end=' ')
    print()