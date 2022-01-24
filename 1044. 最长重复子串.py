class Solution:

    def isRepeat(self, orig:str, sub:str) ->bool:
        return orig.find(sub) != orig.rfind(sub)
    def longestDupSubstring(self, s: str) -> str:
        str_length = len(s)
        max_repeat_arr = [[0,0] for _ in range(str_length)]
        for i in range(str_length):
            if i == 0 or max_repeat_arr[i - 1][1] == 0:
                if self.isRepeat(s, s[i]) :
                    max_repeat_arr[i] = [i,1]
            else:
                for start in range(max_repeat_arr[i-1][0], i + 1):
                    if self.isRepeat(s, s[start: i + 1]):
                        max_repeat_arr[i] = [start,i-start + 1]
                        break

        ret = [0,0]
        for i in max_repeat_arr:
            if i[1] > ret[1]:
                ret = i
        return s[ret[0]:ret[0] + ret[1]]

if __name__ == '__main__':
    print(Solution().longestDupSubstring("abbbcad"))