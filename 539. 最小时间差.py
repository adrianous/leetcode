from typing import List


class Solution:
    def get_minutes_by_time(self, time_str: str):
        time_arr = time_str.split(':')
        return int(time_arr[0]) * 60 + int(time_arr[1])

    def findMinDifference(self, timePoints: List[str]) -> int:
        new_time_arr = [self.get_minutes_by_time(i) for i in timePoints]
        new_time_arr.sort()
        min_time = min((new_time_arr[-1] - new_time_arr[0]), 1440 - (new_time_arr[-1] - new_time_arr[0]))
        for i in range(0, len(new_time_arr) - 1):
            min_time = min(min_time, (new_time_arr[i + 1] - new_time_arr[i]))
        print(new_time_arr)
        return min_time


if __name__ == '__main__':
    print(Solution().findMinDifference(["00:00", "23:59", "00:00"]))
