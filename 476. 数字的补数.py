class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(32):
            if 1 << i > num:
                return ((1 << i) - 1) ^ num

if __name__ == '__main__':
    print(Solution().findComplement(1))
