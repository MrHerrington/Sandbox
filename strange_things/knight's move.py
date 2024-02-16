move = str(input())
move = [move[i] for i in range(2)]
horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertical = ['8', '7', '6', '5', '4', '3', '2', '1']
matrix = [list('.' for i in range(len(horizontal))) for _ in range(len(vertical))]
for i in range(len(vertical)):
    for j in range(len(horizontal)):
        matrix[horizontal.index(move[0])][vertical.index(move[1])] = 'N'
        check = (vertical.index(move[1]) - i) * (horizontal.index(move[0]) - j)
        if abs(check) == 2:
            matrix[j][i] = '*'
        print(matrix[j][i], end=' ')
    print()
