from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            new_index = (left + right) // 2
            if 0 < new_index < len(arr) - 1:
                if arr[new_index - 1] < arr[new_index] and arr[new_index] > arr[new_index + 1]:
                    return new_index
                elif arr[new_index - 1] < arr[new_index] < arr[new_index + 1]:
                    left = new_index
                elif arr[new_index - 1] > arr[new_index] > arr[new_index + 1]:
                    right = new_index
            if left == right:
                break
        return -1

if __name__ == '__main__':
    print(Solution().peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))
