import re


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        new_path_list = []
        for i in path_list:
            if i:
                if i == '..':
                    if len(new_path_list) > 0:
                        new_path_list.pop()
                elif i != '.':
                    new_path_list.append(i)
        return '/'+'/'.join(new_path_list)


if __name__ == '__main__':
    print(Solution().simplifyPath('/.'))
