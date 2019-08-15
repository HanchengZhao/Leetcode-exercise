class Solution:
    def findRedundantConnection(self, edges):
        if not edges:
            return []
        self.extra = []
        parents = [i for i in range(len(edges)+1)]

        def find(x):
            if parents[x] != x:
                # @@@ find recursively
                return find(parents[x])
            return parents[x]

        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                self.extra = [x, y]
                return
            parents[xroot] = parents[yroot]

        for a, b in edges:
            union(a, b)
        return self.extra


s = Solution()

print(s.findRedundantConnection([[1, 2], [2, 3], [1, 3]]))
