from typing import List
from collections import Counter


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        counts = Counter(nums[:k + 1])
        if max([v for _, v in counts.items()]) > 1:
            return True
        for i in range(0, len(nums) - k - 1):
            counts[nums[i]] -= 1
            counts[nums[i + k + 1]] += 1
            if counts[nums[i + k + 1]] > 1:
                return True
        return False


if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1, 1, 3], 1))
