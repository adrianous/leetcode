from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_num = 0
        for i in nums:
            max_num |= i
        l = len(nums)
        ret = 0
        for i in range(2 ** l):
            index = 1
            tmp_num = 0
            for j in range(l):
                a = i & (index << j)
                if a != 0:
                    tmp_num |= nums[j]
            if tmp_num == max_num:
                ret += 1
        return ret


if __name__ == '__main__':
    print(Solution().countMaxOrSubsets([2,2,2]))

