from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        off_arr = [i-v for i, v in enumerate(nums)]
        print(off_arr)
        k = 4
        k = 1
        k = 0
        k = 1
        k = 1




if __name__ == '__main__':
    print(Solution().bestRotation(nums=[3, 2, 1, 4, 0]))
