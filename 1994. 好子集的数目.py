from typing import List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        nums_arr = [0] * 31
        ignores = (4, 8, 9, 16, 18, 20, 24, 25, 27)
        n_l = len(nums)
        for i in range(1, 31):
            nums_arr[i] += 1



