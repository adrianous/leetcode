import math
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(math.gcd(len(nums),k)):
            tmp = nums[i]
            key = i
            while True:
                tmp_key = key + k
                while tmp_key >= len(nums):
                    tmp_key = tmp_key - len(nums)
                if tmp_key == i:
                    nums[key] = tmp
                    break
                nums[key] = nums[tmp_key]
                key = tmp_key
        print(nums)


Solution().rotate([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
