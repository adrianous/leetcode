from collections import defaultdict
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        rec_dic = defaultdict(int)
        area_sum = 0
        for i in rectangles:
            key1 = str(i[0]) + '_' + str(i[1])
            key2 = str(i[2]) + '_' + str(i[3])
            key3 = str(i[0]) + '_' + str(i[3])
            key4 = str(i[2]) + '_' + str(i[1])
            rec_dic[key1] = 1 - rec_dic[key1]
            rec_dic[key2] = 1 - rec_dic[key2]
            rec_dic[key3] = 1 - rec_dic[key3]
            rec_dic[key4] = 1 - rec_dic[key4]
            if rec_dic[key1] == 0:
                del rec_dic[key1]
            if rec_dic[key2] == 0:
                del rec_dic[key2]
            if rec_dic[key3] == 0:
                del rec_dic[key3]
            if rec_dic[key4] == 0:
                del rec_dic[key4]
            area_sum += (i[2] - i[0]) * (i[3] - i[1])
        print(rec_dic.items())
        if len(rec_dic) != 4:
            return False
        xs, ys = [], []

        for k in rec_dic:
            arr = k.split('_')
            xs.append(int(arr[0]))
            ys.append(int(arr[1]))
        return area_sum == (max(ys) - min(ys)) * (max(xs) - min(xs))


if __name__ == '__main__':
    print(Solution().isRectangleCover(
        [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]))
