import functools
from functools import lru_cache


class Solution:

    # def dfs(self, n, k, row, column):
    @functools.lru_cache
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if row < 0 or row >= n or column < 0 or column >= n:
            return 0
        if k == 0:
            return 1
        points = [(row - 1, column + 2), (row - 1, column - 2), (row + 1, column - 2), (row + 1, column + 2),
                  (row - 2, column + 1), (row - 2, column - 1), (row + 2, column - 1), (row + 2, column + 1)]

        return sum(self.knightProbability(n, k - 1, n_row, n_col) / 8 for n_row, n_col in points)


if __name__ == '__main__':
    print(Solution().knightProbability(3, 2, 0, 0))