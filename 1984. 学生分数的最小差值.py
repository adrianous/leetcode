from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        ret = 10 ** 5
        for i in range(0, len(nums) - k + 1):
            ret = min(ret, nums[i + k - 1] - nums[i])
        print(ret)


if __name__ == '__main__':
    print(Solution().minimumDifference([1], 1))
