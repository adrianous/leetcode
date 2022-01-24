import math
from cmath import sqrt


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        end = math.floor(math.sqrt(num))
        ret = 1
        for i in range(2, end + 1):
            if num % i == 0:
                ret += i
                if i ** 2 != num:
                    ret += num // i
        return ret == num

if __name__ == '__main__':
    print(Solution().checkPerfectNumber(28))