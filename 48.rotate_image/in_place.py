class Solution:
    def rotate(self, A):
        n = len(A)
        A.reverse()
        for i in xrange(n):
            for j in xrange(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]