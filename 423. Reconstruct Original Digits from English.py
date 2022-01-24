from collections import defaultdict


class Solution:
    def originalDigits(self, s: str) -> str:
        dic = defaultdict(int)
        for i in s:
            dic[i] += 1
        nums_str = (
            ('zero', '0'), ('two', '2'), ('eight', '8'), ('four', '4'), ('three', '3'), ('one', '1'), ('six', '6'), ('five', '5'),
            ('seven', '7'),
            ('nine', '9'))

        for i in nums_str:
            dic[i] += 1

        nums_list = list()
        for i in nums_str:
            min_count = min([dic[j] for j in i[0]])
            if min_count > 0:
                nums_list.extend([i[1]] * min_count)
                for j in i[0]:
                    dic[j] -= min_count

        return ''.join(sorted(nums_list))

if __name__ == '__main__':
    print(Solution().originalDigits("fviefuro"))