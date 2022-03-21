from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ret = [i for i in range(len(grid[0]))]
        for line in grid:
            for pos_index in range(len(ret)):
                pos = ret[pos_index]
                if pos != -1:
                    if (pos == 0 and line[0] == -1) or (pos == len(ret) - 1 and line[-1] == 1) or (
                            0 <= pos < len(ret) - 1 and line[pos] == 1 and line[pos + 1] == -1) or (
                            0 < pos <= len(ret) - 1 and line[pos] == -1 and line[pos - 1] == 1):
                        ret[pos_index] = -1
                    else:
                        ret[pos_index] += 1 if line[pos] == 1 else -1
        return ret


if __name__ == '__main__':
    print(Solution().findBall([[1, 1, 1, -1, -1],
                               [1, 1, 1, -1, -1],
                               [-1, -1, -1, 1, 1],
                               [1, 1, 1, 1, -1],
                               [-1, -1, -1, -1, -1]]))
