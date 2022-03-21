from typing import List


class Solution:

    def dfs(self,nums, start, end):
        length = end - start + 1
        if length == 1:
            return nums[start]
        if length %2 == 0:
            print('出错了')
            return
        mid = (start + end) // 2
        if (length - 1)//2 % 2 == 0 :
            if nums[mid] == nums[mid + 1]:
                return self.dfs(nums, mid + 2, end)
            else:
                return self.dfs(nums, start, mid)
        else:
            if nums[mid] == nums[mid + 1]:
                return self.dfs(nums, start, mid -1)
            else:
                return self.dfs(nums, mid +1, end)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return self.dfs(nums,0,len(nums) -1)


if __name__ == '__main__':
    print(Solution().singleNonDuplicate([1, 1, 2,2, 3, 3, 4, 4 ,7,8, 8,10,10]))