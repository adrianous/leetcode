from typing import List

import numpy as np


class Graph(object):
    def __init__(self, G):
        self.color = [0] * len(G)
        self.G = G
        self.isDAG = True
        self.circle_count = 0

    def graph_preprocessing(self):
        index = []
        for i in range(len(self.G)):
            if np.sum(self.G[:i]) == 0 and np.sum(self.G[i::]) == 0:
                index.append(i)
        self.G = np.delete(self.G, index, axis=1)
        self.G = np.delete(self.G, index, axis=0)
        self.color = [0] * len(self.G)
        self.satisfy_count = 0

    def DFS(self, i):
        self.color[i] = 1
        num = 0
        for j in range(len(self.G)):
            if self.G[i][j] != 0:
                if self.color[j] == 1:
                    self.circle_count = self.circle_count + 1
                    self.isDAG = False
                    num += 1
                elif self.color[j] == -1:
                    continue
                else:
                    num += self.DFS(j)
        self.color[i] = -1
        return num

    def DAG(self):
        for i in range(len(self.G)):
            if self.color[i] == 0:
                print(i)
                self.DFS(i)
        return self.circle_count


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        arr = np.zeros((n, n))
        for i in requests:
            arr[i[0]][i[1]] += 1
        print(arr)
        # g = Graph(arr)
        # g.graph_preprocessing()
        # return g.DAG()


if __name__ == '__main__':
    print(Solution().maximumRequests(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]))
