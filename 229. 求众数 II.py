from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2, count1, count2 = 0, 0, 0, 0

        for i in nums:
            if i == num1:
                count1 += 1
            elif i == num2:
                count2 += 1
            elif count1 == 0:
                num1 = i
                count1 += 1
            elif count2 == 0:
                num2 = i
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        ret = []
        count1 = 0
        count2 = 0
        for i in nums:
            if i == num1:
                count1 += 1
            elif i == num2:
                count2 += 1
        if count1 > len(nums)/3:
            ret.append(num1)
        if count2 > len(nums)/3:
            ret.append(num2)
        return ret

if __name__ == '__main__':
    print(Solution().majorityElement([1]))

