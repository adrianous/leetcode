import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dic = collections.defaultdict(int)
        s1_l = len(s1)
        for i in s1:
            dic[i] += 1
        diff = len(dic)

        if diff == 0:
            return True
        for i in range(0, len(s2)):
            if i >= s1_l:
                dic[s2[i - s1_l]] += 1
                a = dic[s2[i - s1_l]]
                if a == 0:
                    diff -= 1
                elif a == 1:
                    diff += 1

            dic[s2[i]] -= 1
            a = dic[s2[i]]

            if a == 0:
                diff -= 1
            elif a == -1:
                diff += 1
            if diff == 0:
                return True
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion('ab', "a"))
