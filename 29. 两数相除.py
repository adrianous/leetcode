class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1
        if dividend * divisor < 0:
            flag = -1
        n_dividend = abs(dividend)
        n_divisor = abs(divisor)
        x = n_divisor
        ret = 0
        bottom = x
        while x <= n_dividend:
            bottom = x
            ret += ret or 1
            x += x
        if ret == 0:
            return ret * flag
        return ret * flag + self.divide(dividend - bottom * (1 if dividend >= 0 else -1), divisor)


print(Solution().divide(1, 1))
