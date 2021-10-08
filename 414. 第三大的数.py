from typing import List
import numpy as np

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        big = np.iinfo(np.int32).min
        mid = big
        small = mid
        for i in nums:
            if i > big:
                big = i
            elif i > mid:
                mid = i
            elif i > small:
                small = i

        if small == np.iinfo(np.int32).min:
            return big
        return small


if __name__ == '__main__':
    print(float('-inf'M))