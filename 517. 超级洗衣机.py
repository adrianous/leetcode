from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        sum_machine = sum(machines)
        length = len(machines)
        avg = sum_machine // length
        if avg * length != sum_machine:
            return -1
        target_list = list(map(lambda x: x - avg, machines))
        max_num = max(target_list)
        for i in range(length - 1):
            max_num = max(max_num, abs(target_list[i]))
            target_list[i + 1] += target_list[i]
        return max_num


if __name__ == '__main__':
    print(Solution().findMinMoves([0,3,0]))
