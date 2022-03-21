from collections import defaultdict
from typing import List, Counter


class DetectSquares:

    def __init__(self):
        self.map = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        self.map[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        ret = 0
        x, y = point
        if x not in self.map:
            return ret

        for i in self.map[x]:
            if i != y:
                ret += self.map[x][i] * self.map[x + (y - i)][i] * self.map[x + (y - i)][y]
                ret += self.map[x][i] * self.map[x + (i-y)][i] * self.map[x + (i-y)][y]
        return ret
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
