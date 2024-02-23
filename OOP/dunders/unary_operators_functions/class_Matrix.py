class Matrix:
    def __init__(self, rows, cols, value=0):
        self._rows = rows
        self._cols = cols
        self._value = value
        self._matrix = [list(self._value
                             for _ in range(cols))
                        for _ in range(rows)]

    def __pos__(self):
        return Matrix(self._rows, self._cols, self._value)

    def __neg__(self):
        return Matrix(self._rows, self._cols, -self._value)

    def __invert__(self):
        return Matrix(self._cols, self._rows, self._value)

    def __round__(self, n=None):
        return Matrix(self._rows, self._cols, round(self._value, n))

    def __str__(self):
        return '\n'.join(' '.join(map(str, rows)) for rows in self._matrix)

    def __repr__(self):
        return f'Matrix({self._rows}, {self._cols}, {self._value})'

    def get_value(self, row, col):
        return self._matrix[row][col]

    def set_value(self, row, col, value):
        self._matrix[row][col] = value

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols


# TEST_1:
print(Matrix(2, 3))

# TEST_2:
matrix = Matrix(2, 3, 1)

print(+matrix)
print()
print(-matrix)

# TEST_3:
matrix = Matrix(2, 3)

print(matrix.get_value(0, 0))
print(matrix.get_value(1, 1))

matrix.set_value(0, 0, 100)
matrix.set_value(1, 1, 200)

print(matrix.get_value(0, 0))
print(matrix.get_value(1, 1))

# TEST_4:
matrix1 = Matrix(4, 2)
matrix2 = Matrix(10, 20, value=6)

print(repr(matrix1))
print(repr(matrix2))

# TEST_5:
matrix = Matrix(2, 3, 1)

round_matrix = round(matrix)
plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(round_matrix is matrix)
print(plus_matrix is matrix)
print(minus_matrix is matrix)
print(invert_matrix is matrix)

# TEST_6:
matrix = Matrix(2, 3, 1)

plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(plus_matrix.cols, plus_matrix.rows)
print(minus_matrix.cols, minus_matrix.rows)
print(invert_matrix.cols, invert_matrix.rows)
