import math
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        seq = [math.inf] * 2
        for i in nums:
            if i > seq[1]:
                return True
            elif i > seq[0]:
                seq[1] = i
            else:
                seq[0] = i
        return False



if __name__ == '__main__':
    print(Solution().increasingTriplet([6, 5, 4, 2, 9, 7, 4]))
