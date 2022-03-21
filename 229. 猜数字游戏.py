from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        num_dict = defaultdict(int)
        length = len(secret)
        num_a = 0
        for i in range(length):
            if secret[i] == guess[i]:
                num_a += 1
            else:
                num_dict[secret[i]] += 1
                num_dict[guess[i]] -= 1
        s = sum([abs(tmp) for tmp in num_dict.values()])
        return str(num_a) + 'A' + str(((length - num_a) * 2 - s) // 2) + 'B'


if __name__ == '__main__':
    Solution().getHint()