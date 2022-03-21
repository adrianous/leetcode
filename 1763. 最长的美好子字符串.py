class Solution:

    def isNice(self,s):
        a = [0] *26
        for i in s:
            char_ord = ord(i)
            if char_ord < 97:
                a[char_ord-65] |= 1
            else:
                a[char_ord-97] |= 2
        for i in a:
            if i == 1 or i == 2:
                return False
        return True

    def longestNiceSubstring(self, s: str) -> str:
        max_ret = ''
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if self.isNice(s[i:j+1]):
                    if j-i+1 > len(max_ret):
                        max_ret = s[i:j+1]
        return max_ret

if __name__ == '__main__':
    print(Solution().isNice('aAa'))
    print(Solution().longestNiceSubstring("aAa"))