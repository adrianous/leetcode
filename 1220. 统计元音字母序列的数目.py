class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp, M = [1] * 5, 10 ** 9 + 7
        for i in range(1, n):
            dp = [dp[1] % M, (dp[0] + dp[2]) % M, (dp[0] + dp[1] + dp[3] + dp[4]) % M, (dp[2] + dp[4]) % M, dp[0] % M]
        return sum(dp) % M
