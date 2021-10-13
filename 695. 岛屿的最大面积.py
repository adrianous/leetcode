from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        w, h = len(grid[0]), len(grid)
        mark_grid = [[False for _ in range(w)] for _ in range(h)]
        ret = 0

        def update_mark_grid(_mark_grid, _grid, x, y):
            _ret = 0
            if x < 0 or x >= w or y < 0 or y >= h or _grid[y][x] == 0 or _mark_grid[y][x]:
                return _ret
            _mark_grid[y][x] = True
            _ret += 1
            _ret += update_mark_grid(_mark_grid, _grid, x + 1, y)
            _ret += update_mark_grid(_mark_grid, _grid, x - 1, y)
            _ret += update_mark_grid(_mark_grid, _grid, x, y + 1)
            _ret += update_mark_grid(_mark_grid, _grid, x, y - 1)
            return _ret

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    ret = max(ret, update_mark_grid(mark_grid, grid, j, i))
        return ret


if __name__ == '__main__':
    print(Solution().maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
