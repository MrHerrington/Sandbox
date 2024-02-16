def transpose(_matrix):
    new_matrix = []
    for i in range(max(map(len, _matrix))):
        temp = []
        for j in range(len(_matrix)):
            temp.append(_matrix[j][i])
        new_matrix.append(temp[:])
        temp.clear()
    return new_matrix


matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10]]
for row in transpose(matrix):
    print(row)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for row in transpose(matrix):
    print(row)
