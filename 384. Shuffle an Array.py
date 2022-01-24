import copy
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self._nums = nums

    def reset(self) -> List[int]:
        return self._nums

    def shuffle(self) -> List[int]:
        copy_nums = copy.deepcopy(self._nums)
        ret = []
        while len(copy_nums) > 0:
            ret.append(copy_nums.pop(random.randint(0, len(copy_nums)-1)))
        return ret

# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3,4,5,6,7,8,9])
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)
print(obj.shuffle())
