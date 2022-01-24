class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n):
            for j in range(1, n + 1):
                if j + i <= n:
                    if i == 1:
                        dp[j][j + i] = j
                    elif i == 2:
                        dp[j][j + i] = j + 1
                    else:
                        dp[j][j + i] = min(
                            [max(dp[j][x-1], dp[x + 1][j + i]) + x for x in range(j, j + i)])
                else:
                    break

        return dp[1][n]


if __name__ == '__main__':
    print(Solution().getMoneyAmount(55))

1, 2, 3, 4, 5, 6
