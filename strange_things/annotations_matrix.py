from typing import List, Union


def matrix_to_dict(matrix_: List[List[Union[int, float]]]) -> dict:
    return {i + 1: matrix_[i] for i in range(len(matrix_))}


matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
print(matrix_to_dict(matrix))
