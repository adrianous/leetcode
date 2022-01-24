from functools import lru_cache


class Solution:
    def integerReplacement(self, n: int) -> int:
        # times_array = [0] * (n + 2)
        # times_array[1] = 0
        # for i in range(2, n + 1):
        #     if i % 2 == 0:
        #         times_array[i] = times_array[i // 2] + 1
        #     else:
        #         times_array[i] = min(times_array[i - 1] + 1, times_array[(i + 1) // 2] + 2)
        #     print(times_array)
        # return times_array[n]
        @lru_cache
        def dfs(num):
            ret = 1
            if num == 1:
                return 0
            if num % 2 == 0:
                ret += dfs(num // 2)
            else:
                ret += min(dfs(num - 1), dfs(num + 1))
            return ret

        return dfs(8)

if __name__ == '__main__':
    print(Solution().integerReplacement(8))
