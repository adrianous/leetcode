from typing import List
from collections import  Counter
import re

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        print(re.sub("\d|\s","", licensePlate))

        map_arr = [0] * 26



if __name__ == '__main__':
    print(Counter("abcddd"))
    Solution().shortestCompletingWord("ab c112 DF 31v1z4 a2", ["abc", 'abda'])
