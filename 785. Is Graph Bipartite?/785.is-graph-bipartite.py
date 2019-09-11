#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # use 0 and 1 to separate
        color = {}

        def dfs(pos):
            for neib in graph[pos]:
                if neib in color:
                    if color[neib] == color[pos]:
                        return False
                else:
                    # use a different color
                    color[neib] = 1 - color[pos]
                    if not dfs(neib):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                # traverse its neighbors to see if they have different color
                if not dfs(i):
                    return False
        return True
# time : O(V + E)
# space: O(V)
# topic: dfs, graph
