import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        remain_apples = []
        ret = 0
        for i in range(len(apples)):
            if apples[i] != 0:
                new_remain = [days[i], apples[i]]
                for j in remain_apples:
                    if j[0] == days[i]:
                        j[1] += apples[i]
                        break
                else:
                    remain_apples.append(new_remain)
            if len(remain_apples) > 0:
                ret += 1
            else:
                continue
            min_day_apple = remain_apples[0]
            for j in remain_apples:
                j[0] -= 1
                if j[0] == 0:
                    min_day_apple = j
                if j[0] < min_day_apple[0]:
                    min_day_apple = j
            min_day_apple[1] -= 1
            if min_day_apple[0] == 0 or min_day_apple[1] == 0:
                remain_apples.remove(min_day_apple)
        remain_apples.sort()
        eat_days = 0
        for i in remain_apples:
            i[0] -= eat_days
            if i[0] > 0:
                eat_days += min(i)
                ret += min(i)
        return ret


if __name__ == '__main__':
    a = [[1, 3], [4, 5], [2, 2]]
    # print(Solution().eatenApples(
    #     [1, 10, 17, 10, 12, 6, 20, 8, 8, 22, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3,
    #      5, 2, 1, 0, 0, 0, 0, 0, 0, 23],
    #     [19999, 11, 18, 22, 5, 2, 14, 5, 20, 7, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2,
    #      1, 4, 2, 7, 0, 0, 0, 0, 0, 0, 1]))
    b = []
    heapq.heappush(b, [1, 2])
    heapq.heappush(b, [5, 3])
    heapq.heappush(b, [2, 2])
    # heapq.heappush(b, [-2, 2])
    print(b)
    print(heapq.heappop(b))
    print(heapq.heappop(b))
    print(heapq.heappop(b))
