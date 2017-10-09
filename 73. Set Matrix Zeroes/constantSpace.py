class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        col0 = 1
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in xrange(rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in xrange(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
                    
        for i in xrange(rows-1, -1, -1):
            for j in xrange(cols-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
'''
store states of each row in the first of that row, and store states of each column in the first of that column. Because the state of row0 and the state of column0 would occupy the same cell, I let it be the state of row0, and use another variable "col0" for column0. In the first phase, use matrix elements to set states in a top-down way. In the second phase, use states to set matrix elements in a bottom-up way.
'''