class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parents = [i for i in range(n)]
        visited = set()
        self.count = 0

        def find(x):
            if parents[x] != x:
                return find(parents[x])
            return parents[x]

        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return
            parents[xroot] = parents[yroot]

        for a, b in edges:
            union(a, b)
        for i in parents:
            p = find(i)
            if p not in visited:
                self.count += 1
            visited.add(p)
        return self.count
