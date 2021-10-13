from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = {}
        for i in paths:
            if i[0] in dic:
                dic[i[0]] += 1
            else:
                dic[i[0]] = 1

            if i[1] in dic:
                dic[i[1]] -= 1
            else:
                dic[i[1]] = -1
            if dic[i[1]] == -1:
                ret = i[1]
        return ret
