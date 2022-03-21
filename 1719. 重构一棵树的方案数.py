import collections
from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)
        ans = 1
        ancestors = set()
        for n in sorted(graph, key=lambda x: -len(graph[x])):
            p = min(ancestors & graph[n], key=lambda x: len(graph[x]), default=None)
            ancestors.add(n)
            if p:
                if graph[n] - (graph[p] | {p}): return 0
                if len(graph[n]) == len(graph[p]): ans = 2
            elif len(graph[n]) != len(graph)-1: return 0
        return ans