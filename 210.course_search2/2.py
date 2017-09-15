from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def dfs(graph, visited, i, res):
            if visited[i] == -1: # has cycle
                return False
            if visited[i] == 1: # has visited
                return True
            visited[i] = -1 # is being visited
            for j in graph[i]:
                if not dfs(graph, visited, j, res):
                    return False
            # reach the end
            res.append(i)
            visited[i] = 1
            return True
        graph = defaultdict(list)
        res = []
        # build the graph
        for i in prerequisites:
            graph[i[0]].append(i[1]) # value is key's prerequisite
        visited = [0] * numCourses
        for i in xrange(numCourses):
            if not dfs(graph, visited, i, res): # dfs here will append candidate node to visited
                return []
        return res
'''
implement topological sort using dfs, use flag to check visited or cyclic
'''