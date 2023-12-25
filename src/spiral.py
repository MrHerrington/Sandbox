n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
x = - 1
y = 0
i = 1
move_column = 1
move_row = 0
while i <= n * m:
    if 0 <= x + move_column < m and 0 <= y + move_row < n and matrix[y + move_row][x + move_column] == 0:
        x += move_column
        y += move_row
        matrix[y][x] = i
        i += 1
    else:
        if move_column == 1:
            move_column = 0
            move_row = 1
        elif move_row == 1:
            move_row = 0
            move_column = - 1
        elif move_column == - 1:
            move_column = 0
            move_row = - 1
        elif move_row == - 1:
            move_row = 0
            move_column = 1
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
