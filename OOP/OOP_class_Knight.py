from copy import deepcopy


class Knight:
    """Класс описывает шахматного коня"""
    def __init__(self, horizontal, vertical, color):
        """horizontal — координата коня по горизонтали, латинская буква от a до h включительно;
        vertical — координата коня по вертикали, целое число от 1 до 8 включительно;
        color — цвет коня (black или white)"""
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.horizontal_vals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.vertical_vals = [8, 7, 6, 5, 4, 3, 2, 1]
        self.matrix = [list('.'
                            for i in range(len(self.horizontal_vals)))
                       for _ in range(len(self.horizontal_vals))]

    def get_char(self):
        """Метод возвращает символ N"""
        return 'N'

    def can_move(self, horizontal, vertical):
        """Метод принимает в качестве аргументов координаты клетки по горизонтали
        и по вертикали, и возвращает True, если конь может переместиться на клетку
        с данными координатами, или False в противном случае"""
        check_lst = []
        for i in range(len(self.vertical_vals)):
            for j in range(len(self.horizontal_vals)):
                check_move = (self.vertical_vals.index(vertical) - i) * \
                             (self.horizontal_vals.index(horizontal) - j)
                if abs(check_move) == 2:
                    check_lst.append((j, i))
        return (self.vertical_vals.index(self.vertical),
                self.horizontal_vals.index(self.horizontal)) in check_lst

    def move_to(self, horizontal, vertical):
        """Метод принимает в качестве аргументов координаты клетки по горизонтали
        и по вертикали и заменяет текущие координаты коня на переданные.
        Если конь из текущей клетки не может переместиться на клетку с указанными
        координатами, его координаты остаются неизменными"""
        if Knight.can_move(self, horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def draw_board(self):
        """Метод печатает шахматное поле, отмечает на этом поле коня и клетки, на которые
        может переместиться конь. Пустые клетки должны быть отображены символом . ,
        конь — символом N, клетки, на которые может переместиться конь, — символом * """
        temp_matrix = deepcopy(self.matrix)
        for i in range(len(self.vertical_vals)):
            for j in range(len(self.horizontal_vals)):
                temp_matrix[self.horizontal_vals.index(self.horizontal)] \
                    [self.vertical_vals.index(self.vertical)] = 'N'
                check_move = (self.vertical_vals.index(self.vertical) - i) * \
                             (self.horizontal_vals.index(self.horizontal) - j)
                if abs(check_move) == 2:
                    temp_matrix[j][i] = '*'
                print(temp_matrix[j][i], end=' ')
            print()


knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
knight.draw_board()
print(knight.can_move('e', 4))
knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)
knight.draw_board()
