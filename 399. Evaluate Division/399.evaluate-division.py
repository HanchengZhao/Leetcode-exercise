#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        # build graph
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val

        def findVal(a, b):
            # doesn't exist
            if a not in graph or b not in graph:
                return -1.0
            if a == b:
                return 1.0
            queue = deque([[a, 1.0]])
            visited = set()
            while queue:
                front, cur = queue.popleft()
                if front in visited:
                    continue
                visited.add(front)
                for child, val in graph[front].items():
                    if child == b:
                        return cur * val
                    newvalue = cur * val
                    queue.append([child, newvalue])
                    # path compression
                    graph[a][child] = newvalue
                    graph[child][a] = 1 / newvalue
            return -1.0
        return [findVal(a, b) for a, b in queries]
