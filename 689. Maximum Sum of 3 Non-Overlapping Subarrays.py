from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        max_sum1, sum1, index1 = 0, 0, 0
        max_sum2, sum2, index2 = 0, 0, 0
        max_sum3 = 0
        ret = []
        for i in range(2 * k, len(nums)):
            sum1 += nums[i - 2 * k]
            sum2 += nums[i - k]
            if i >= 3 * k - 1:
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    index1 = i - 2 * k - 1
                if max_sum1 + sum2 > max_sum2:
                    max_sum2 = max_sum1 + sum2
                    index2 = i - k - 1
                if max_sum2 + sum(nums[i - k + 1:i + 1]) > max_sum3:
                    max_sum3 = max_sum2 + sum(nums[i - k + 1:i + 1])
                    ret = [index1, index2, i - k + 1]
                sum1 -= nums[i - 3 * k - 1]
                sum2 -= nums[i - 2 * k - 1]
        return ret


if __name__ == '__main__':
    print(Solution().maxSumOfThreeSubarrays([4,3,2,1], 1))
