class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parents = {i: i for i in range(1, N+1)}
        self.extra = []

        def find(x):
            if parents[x] != x:
                return find(parents[x])
            return parents[x]

        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                self.extra = [x, y]
                return
            parents[xroot] = yroot

        for a, b in edges:
            union(a, b)
        return self.extra

# the basic idea is to union the connected edges, if we found that 2 nodes are already connected,
# they are the extra one
# time: O(n)
