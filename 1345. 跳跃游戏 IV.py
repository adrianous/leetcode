from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        idx_same_value = defaultdict(list)
        for i, a in enumerate(arr):
            idx_same_value[a].append(i)
        visited_index = set()
        q = deque()
        q.append([0, 0])
        visited_index.add(0)

        print(idx_same_value)
        while q:
            idx, step = q.popleft()
            if idx == len(arr) - 1:
                return step
            v = arr[idx]
            step += 1
            for i in idx_same_value[v]:
                if i not in visited_index:
                    visited_index.add(i)
                    q.append([i, step])

            del idx_same_value[v]

            if idx + 1 < len(arr) and (idx + 1) not in visited_index:
                visited_index.add(idx + 1)
                q.append([idx + 1, step])

            if idx - 1 >= 0 and (idx - 1) not in visited_index:
                visited_index.add(idx - 1)
                q.append([idx - 1, step])


if __name__ == '__main__':
    print(Solution().minJumps([7, 6, 9, 6, 9, 6, 9, 7]))
