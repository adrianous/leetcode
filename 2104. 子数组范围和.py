from typing import List


class Solution:
    def subArrayRanges(self, arr: List[int]) -> int:

        ret = 0
        for i, v in enumerate(arr):
            max_v = v
            min_v = v
            print(i, v)
            for j in range(i, len(arr)):
                if arr[j] > max_v:
                    max_v = arr[j]
                if arr[j] < min_v:
                    min_v = arr[j]
                ret += max_v - min_v
        return ret
