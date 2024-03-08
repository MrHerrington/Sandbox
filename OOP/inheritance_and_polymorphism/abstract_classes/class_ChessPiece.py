from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, hor, vert):
        pass


class King(ChessPiece):
    def can_move(self, hor, vert):
        shift = [abs(ord(self.horizontal) - ord(hor)), abs(self.vertical - vert)]
        return max(shift) < 2 and sum(shift) > 0


class Knight(ChessPiece):
    def can_move(self, hor, vert):
        shift = [abs(ord(self.horizontal) - ord(hor)), abs(self.vertical - vert)]
        return max(shift) == 2 and min(shift) == 1


# Test №1
king = King('b', 2)

print(king.can_move('c', 3))
print(king.can_move('a', 1))
print(king.can_move('f', 7))

# Test №2
knight = Knight('h', 8)

print(knight.can_move('h', 8))
print(knight.can_move('a', 6))
print(knight.can_move('a', 1))
print(knight.can_move('g', 6))
