'''
Use dfs to traverse all the possible combinations, but with cached result

Use bit mask to save space

Time: O(n * m), n for count of workers, m for count of bikes
'''


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        cache = {}

        def dis(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        def dfs(i, visited):
            if i == len(workers):
                return 0
            if (i, visited) in cache:
                return cache[(i, visited)]
            res = float("inf")
            for j in range(len(bikes)):
                # if the bike is not taken
                if not visited & 1 << j:
                    res = min(res, dfs(i+1, visited | 1 << j) +
                              dis(workers[i], bikes[j]))
            cache[(i, visited)] = res
            return res
        return dfs(0, 0)
