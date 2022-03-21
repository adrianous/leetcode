from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ret = []
        for i in range(n + 1):
            for j in range(1, i):
                if self.gcd(i, j) == 1:
                    ret.append(str(j) + '/' + str(i))
        return ret


    def gcd(self, a, b):
        if a % b == 0:
            return b
        return self.gcd(b, a % b)


if __name__ == '__main__':
    print(Solution().simplifiedFractions(8))
    print(Solution().gcd(8, 6))
