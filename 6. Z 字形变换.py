class Solution:
    def convert(self, s: str, numRows: int) -> str:
        width = len(s)
        if numRows == 1:
            return s
        height = numRows
        ret = [['' for _ in range(width)] for _ in range(height)]
        x = y = 0
        reverse = False
        for i in s:

            ret[y][x] = i
            if reverse:
                y -= 1
                x += 1
            else:
                y += 1

            if y == height:
                reverse = True
                y = height - 2
                x += 1
            if y == 0:
                reverse = False
        return ''.join([''.join(j) for j in ret])



if __name__ == '__main__':
    print(Solution().convert('abcdefghi', 2))
