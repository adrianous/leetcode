from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x_len = len(matrix)
        if x_len == 0:
            return False
        y_len = len(matrix[0])
        if y_len == 0:
            return False

        x, y = 0, y_len - 1
        while x < x_len and y >= 0:
            tmp = matrix[x][y]
            if tmp == target:
                return True
            elif tmp > target:
                y -= 1
            else:
                x += 1
        return False


if __name__ == '__main__':
    x, y = (1, 2)
    print(x)
