from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height) -1
        mark_left = left
        mark_right = right
        max_area = 0
        while left < right:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
