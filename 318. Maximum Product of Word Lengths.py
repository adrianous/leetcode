from collections import defaultdict
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        nums = defaultdict(int)
        for i in words:
            num = 0
            for j in i:
                num |= 1 << ord(j) - ord('a')
            nums[num] = max(nums[num], len(i))
        print(nums)
        ret = 0
        for k_o, v_o in nums.items():
            for k_i, v_i in nums.items():
                if k_i & k_o == 0:
                    ret = max(ret, v_o * v_i)

        return ret

if __name__ == '__main__':
    print(Solution().maxProduct(['abc', 'bca', 'yuoujo']))
