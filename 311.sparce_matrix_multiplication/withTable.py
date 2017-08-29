class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # use a table to store the non-zero num in B
        tableB = {}
        if len(A) == 0:
            return []
        m, n = len(A), len(A[0])
        if len(B) != n:
            raise Exception("A's col number is not equal to B's row number")
        k = len(B[0])
        res = [[0] * k for i in xrange(m)] # A' col num and B' row num
        for i in xrange(n):
            for j in xrange(k):
                if B[i][j] != 0:
                    tableB[(i,j)] = B[i][j] # update table
        # loop over A
        for i in xrange(m):
            for j in xrange(n):
                if A[i][j] != 0:
                    for p in xrange(k):
                        if (j,p) in tableB:
                            res[i][p] += A[i][j] * tableB[(j,p)]
        return res