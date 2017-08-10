class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return [[]]
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            raise Exception("A's column number should be equal to B's column number")
        res = [[0] * l for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if A[i][j] != 0:
                    for k in xrange(l):
                        if B[j][k] != 0:
                            res[i][k] += A[i][j] * B[j][k]
        return res

'''
this is a solution without using hashtable, so the basic idea is to traverse
every element in A and B matrix, but skip when either is 0, which saves a lot 
in sparce matrix example
'''

