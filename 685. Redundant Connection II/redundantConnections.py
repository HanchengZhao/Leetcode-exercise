#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#

'''
3 invalid situations
case1: 2 parents no circle

  1
 / \ 
v   v
2 -->3

case2: 2 parents with circle
case3: 1 parent with circle

we can 1 enumerate together, check if there's a loop or a node with 2 parents

record, circleEdge, criticalEdge and the edge that 
2 main steps
1 check whether there exists a node with 2 parents, if yes, store the two edges.
2 if no edge yielded from step 1, apply union-find and 
find the edge creating cycle (same as 684); 
ELSE, apply union-find to ALL edges EXCEPT edges from step 1, then check: 
if edge 1 from step 1 creates a cycle, return edge 1; else return edge 2.

https://leetcode.com/problems/redundant-connection-ii/discuss/254733/Python-Union-Find-Clear-Logic
'''


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n+1)]

        def find(x):
            if parents[x] != x:
                return find(parents[x])
            return parents[x]

        def union(a, b):
            aroot, broot = find(a), find(b)
            if aroot == broot:
                # find a circle
                return False
            parents[aroot] = parents[broot]
            return True

        # return 2 candidate edges that result in a node having 2 parents
        def findNodeWith2Parents(edges):
            # to, from
            path_from = {}
            for a, b in edges:
                if b not in path_from:
                    path_from[b] = a
                else:
                    # WATCHOUT: should put the previous visited edge ahead
                    # so we can skip cand2, otherwise we shall skip cand1
                    return [path_from[b], b], [a, b]
            return None, None

        cand1, cand2 = findNodeWith2Parents(edges)

        # check if there are circles
        for x, y in edges:
            # skip cand2 for now
            if [x, y] == cand2:
                continue
            # find a circle when cand1 in the loop
            if not union(x, y):
                if cand1:
                    return cand1
                else:
                    return [x, y]
        # no circle exists if we eliminate cand2, so the bad edge is cand2
        return cand2
