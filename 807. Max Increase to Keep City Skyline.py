from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        height, width = [max(i) for i in grid], [max([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret += min(height[i], width[j]) - grid[i][j]
        return ret




if __name__ == '__main__':
    print(Solution().maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
