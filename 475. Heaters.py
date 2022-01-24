from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        tmp = []
        min_index = 0
        houses.sort()
        heaters.sort()
        for i in houses:
            min_range = 10 ** 10

            for j in range(min_index, len(heaters)):
                if abs(heaters[j] - i) <= min_range:
                    min_range = abs(heaters[j] - i)
                    min_index = j
                else:
                    break
            tmp.append((i, heaters[min_index]))
        print(tmp)
        return max([abs(i[0] - i[1]) for i in tmp])


if __name__ == '__main__':
    print(Solution().findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],
[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]))
