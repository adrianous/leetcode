from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        ret = 0
        for i in range(len(nums)):
            while nums[i] - nums[left] > 1:
                left += 1
            if nums[i] - nums[left] == 1:
                ret = max(ret, i - left + 1)
        return ret


if __name__ == '__main__':
    print(Solution().findLHS(
        [2555, 8384, 5240, 4555, 8819, 7305, 8410, 258, -7449, 4335, -3603, 262, 1910, 8841, 2351, 4975, 7966, 2880,
         3577, -2064, -6012, 6006, 3005, 8761, 1201, 8560, 8972, 1389, 6682, 3284, 2510, 8517, -2763, 7679, 7856, -116,
         9812, 9220, 283, 2952, 5816, 2078, 3342, -3030, 1367, 6414, -8579, 1538, 125, -8117, -8918, 3961, -7658, 1269,
         1626, 9745, 7729, 2179, 6126, 3626, -3276, 490, 858, 9888, 1931, 4636, 7529, -6978, 8108, 3561, 1819, -6023,
         -5574, 2285, -7045, -4768, 2623, 9150, 62, 7117, 9966, 256, -6203, -5524, 3759, 2505, 4720, 286, 4307, 5730,
         8269, 7899, 4781, -7409, 2659, 9135, 2643, -3510, 5107, 3367, 8247, 322, -1006, 816, -7627, 8842, 2297, 4889,
         4740, 3409, 263, 7731, 9997, -898, 6459, 9777, 2497, 2598, 998, 8, 7361, 6587, 1199, 8253, 3119, 2956, 4268,
         -8398, 1175, 5240, 8486, 2844, 1742, 8458, 1063, 9273, 2417, 9077, 3441]))
