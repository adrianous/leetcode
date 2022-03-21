from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left_l = [-1] * len(s)
        right_l = [-1] * len(s)
        pre_sum = [0] * len(s)
        sum_t = 0
        left = -1
        for i, v in enumerate(s):
            if v == '*':
                sum_t += 1
            else:
                left = i
            left_l[i] = left
            pre_sum[i] = sum_t
        right = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '|':
                right = i
            right_l[i] = right
        ret = []
        for s, e in queries:
            x, y = right_l[s], left_l[e]
            if 0 <= x < y and y >= 0:
                ret.append(pre_sum[y] - pre_sum[x])
            else:
                ret.append(0)
        return ret


if __name__ == '__main__':
    print(Solution().platesBetweenCandles("***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))
