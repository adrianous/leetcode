from typing import List, Set


class Solution:
    def dfs(self, grid: List[List[int]], row: int, col: int, color: int, mark_hash: List[List[int]], mark_color: int):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return False
        if mark_hash[row][col] == 1:
            return True
        if grid[row][col] != mark_color:
            return False
        mark_hash[row][col] = 1
        b1 = self.dfs(grid, row - 1, col, color, mark_hash, mark_color)
        b2 = self.dfs(grid, row, col - 1, color, mark_hash, mark_color)
        b3 = self.dfs(grid, row + 1, col, color, mark_hash, mark_color)
        b4 = self.dfs(grid, row, col + 1, color, mark_hash, mark_color)
        print("*****************************")

        if not (b1 and b2 and b3 and b4):
            grid[row][col] = color
        print('====================')
        print(grid)

        return True

    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        mark_hash = [[0] * len(grid[0]) for _ in range(len(grid))]
        mark_color = grid[row][col]
        self.dfs(grid, row, col, color, mark_hash, mark_color)
        return grid


if __name__ == '__main__':
    print(Solution().colorBorder([[1,1,1],[1,1,1],[1,1,1]], 1, 1, 3))
