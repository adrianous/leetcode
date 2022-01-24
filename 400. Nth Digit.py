import math


class Solution:
    def findNthDigit(self, n: int) -> int:
        ex = 0
        n -= 1
        start_num = 9 * (10 ** ex) * (ex+1)
        while n > start_num:
            n -= start_num
            ex += 1
            start_num = 9 * (10 ** ex) * (ex + 1)
        num = 10 ** ex + math.floor(n / (ex + 1))
        n_num_index = n % (ex + 1)
        return int(str(num)[n_num_index])


if __name__ == '__main__':
    print(Solution().findNthDigit(1000))