class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        cursor = 0
        if len(dominoes) == 1:
            return dominoes
        dominoes = list(dominoes)
        while cursor < len(dominoes):
            if dominoes[cursor] == 'R':
                for i in range(cursor + 1, len(dominoes)):
                    if dominoes[i] == 'R':
                        dominoes[cursor + 1:i + 1] = 'R' * (i - cursor)
                        cursor = i
                        break
                    if dominoes[i] == 'L':
                        dominoes[cursor:i + 1] = 'R' * ((i + 1 - cursor) // 2) + '.' * ((i + 1 - cursor) % 2) + 'L' * ((
                                    i + 1 - cursor) // 2)
                        cursor = i + 1
                        break
                else:
                    dominoes[cursor:] = 'R' * (len(dominoes) - cursor)
                    cursor += 1
            elif dominoes[cursor] == 'L':
                for i in range(cursor - 1, -1, -1):
                    if dominoes[i] == 'R':
                        cursor += 1
                        break
                    if dominoes[i] == 'L':
                        cursor += 1
                        dominoes[i:cursor] = 'L' * (cursor - i)
                        break
                else:
                    dominoes[0:cursor] = 'L' * cursor
                    cursor += 1
            else:
                cursor += 1
        return ''.join(dominoes)

if __name__ == '__main__':
    print(Solution().pushDominoes("LR"))
    # a = ['a', 'b', 'c', 'd']
    # a[:3] = 'a' * 3 + 'c' * 0 + 'b' * 3
    # print(a)