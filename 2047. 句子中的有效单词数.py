import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        arr = sentence.split()

        ret = 0
        for word in arr:
            if word[0] == '-' or word[-1] == '-' or word.count('-') > 1:
                continue
            if '!' in word[0:-1] or '.' in word[0:-1] or ',' in word[0:-1]:
                continue
            if len(word)> 1 and  word[-2] == '-' and ('!' == word[-1] or ',' == word[-1] or '.' == word[-1]):
                continue
            if re.search('\d', word):
                continue
            ret +=1
        return ret



if __name__ == '__main__':
    print(Solution().countValidWords('aa  asdfasdf,wefawea  123a q-. s'))