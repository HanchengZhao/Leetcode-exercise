from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(graph, visited, i):
            if visited[i] == -1: # there is cycle detected
                return False
            if visited[i] == 1: # has been visited
                return True 
            visited[i] = -1 # marked as being visited
            for j in graph[i]:
                if not dfs(graph, visited, j):
                    return False
            visited[i] = 1 # marked as visited
            return True
        visited = [0] * numCourses
        graph = defaultdict(list)
        # initialize the graph
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        for i in xrange(numCourses):
            if not dfs(graph, visited, i):
                return False
        return True

'''
use dfs to check if there is cycle inside the graph
'''