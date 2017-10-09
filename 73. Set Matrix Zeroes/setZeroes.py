class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        rows = [False] * len(matrix)
        cols = [False] * len(matrix[0])
        
        for i in xrange(len(rows)):
            for j in xrange(len(cols)):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        for i in xrange(len(rows)):
            for j in xrange(len(cols)):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
# space: O(m + n)                    