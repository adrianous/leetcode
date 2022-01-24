class Solution:
    def countAndSay(self, n: int) -> str:
        num_str = '1'
        for i in range(2, n+1):
            cur_index = 0
            new_num = ''
            while cur_index < len(num_str):
                num = num_str[cur_index]
                count = 0
                while cur_index < len(num_str) and num_str[cur_index] == num:
                    count += 1
                    cur_index += 1
                new_num += str(count) + num
            num_str = new_num
        return num_str

if __name__ == '__main__':
    for i in range(1, 10):
        print(Solution().countAndSay(i))
