from typing import List


class SummaryRanges:

    def __init__(self):
        self._ret = []

    def addNum(self, val: int) -> None:
        for i in range(len(self._ret)):
            data = self._ret[i]
            if data[0] <= val <= data[1]:
                return
            if val < data[0] - 1:
                if i == 0 or val > self._ret[i - 1][1] + 1:
                    self._ret.insert(i, [val, val])
                    return
            if data[0] == val + 1:
                data[0] = val
                return
            elif data[1] == val - 1:
                data[1] = val
                if i + 1 < len(self._ret) and self._ret[i + 1][0] <= data[1] + 1:
                    data[1] = self._ret[i + 1][1]
                    self._ret.pop(i + 1)
                return
        self._ret.append([val, val])

    def getIntervals(self) -> List[List[int]]:
        return self._ret


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(1)
obj.addNum(3)
obj.addNum(7)
obj.addNum(2)
obj.addNum(6)
param_2 = obj.getIntervals()
print(param_2)
