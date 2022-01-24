import random

from typing import List


class Solution:
    def get_dif_alpha(self, s: List[str], pos: int) -> str:
        same_list = []
        if pos > 0:
            same_list.append(s[pos - 1])
        if pos < len(s) - 1 and s[pos + 1] != '?':
            same_list.append(s[pos + 1])

        while chr(a := random.randrange(ord('a'), ord('z') + 1)) in same_list:
            pass
        return chr(a)

    def modifyString(self, s: str) -> str:
        l = list(s)
        for i in range(len(l)):
            if l[i] == '?':
                l[i] = self.get_dif_alpha(l, pos=i)

        return ''.join(l)


if __name__ == '__main__':
    print(Solution().modifyString("j?qg??b"))
