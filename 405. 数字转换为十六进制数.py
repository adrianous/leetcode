class Solution:
    def toHex(self, num: int) -> str:
        r_n = ""
        while num > 0:
            r_n = str(num % 16) + r_n
            num = num // 16

        return r_n


print(Solution().toHex(88))