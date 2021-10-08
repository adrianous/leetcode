from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        ret = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ret.insert(0, nums[left] * nums[left])
                left += 1
            else:
                ret.insert(0, nums[right] * nums[right])
                right -= 1
        return ret
