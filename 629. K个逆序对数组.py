class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1] + [0 for _ in range(k)]
        for i in range(1, n+1):
            new_dp = dp.copy()
            for j in range(k+1):
                new_dp[j] = (new_dp[j - 1] if j > 0 else 0) + dp[j] - (dp[j - i] if j >= i else 0)
                new_dp[j] %= mod
            dp = new_dp
        return dp[k-1]
