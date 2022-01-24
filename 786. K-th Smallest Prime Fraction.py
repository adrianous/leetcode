from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        return sorted([[arr[i], arr[j]] for i in range(len(arr) - 1) for j in range(i + 1, len(arr))], key=lambda x: x[0] / x[1])[k - 1]

print(Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 3))
