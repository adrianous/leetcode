from typing import List




class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        l = len(nums)
        ret = 0
        for i in range(l):
            for j in range(i + 1, l):
                if j != i and abs(nums[j]-nums[i]) == k:
                    ret += 1
        return ret

