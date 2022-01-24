from typing import List


# nums1 = [4,1,2], nums2 = [1,3,4,2].
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, dic = [], {}
        for i in nums2:
            while stack and stack[len(stack) - 1] < i:
                dic[stack.pop()] = i
            stack.append(i)
        return [dic[i] if i in dic else -1 for i in nums1]

if __name__ == '__main__':
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
