class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def find(roots, i):
            while roots[i] != i: # path compression in the process
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i
        
        roots = range(n)
        for e in edges:
            r1 = find(roots, e[0])
            r2 = find(roots, e[1])
            if r1 != r2:
                roots[r1] = r2 # union
                n -= 1
        return n