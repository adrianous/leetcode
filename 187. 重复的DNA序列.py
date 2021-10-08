import collections
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = 10
        dic = collections.defaultdict(int)
        ret = []
        for i in range(len(s) - l + 1):
            dic[s[i:i + l]] += 1
            if dic[s[i:i + l]] == 2:
                ret.append(s[i:i + l])
        return ret


if __name__ == '__main__':
    print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))