from collections import Counter
class Solution:
    def removeInvalidParentheses(self, num: int) -> bool:
        tmp = 2
        num_count = Counter(list(str(num)))
        while len(str(tmp)) <= len(str(num)):
            if Counter(list(str(tmp))) == num_count:
                return True
            tmp *= 2
        return False

if __name__ == '__main__':
    print(Solution().removeInvalidParentheses(2))
