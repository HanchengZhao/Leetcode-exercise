class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return [[]]
        matrix = [[0]*n for i in xrange(n)]
        rowStart, colStart, rowEnd, colEnd = 0, 0, n-1, n-1
        num = 1
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in xrange(colStart, colEnd+1): #rightward
                matrix[rowStart][i] = num
                num += 1
            rowStart += 1
            for i in xrange(rowStart, rowEnd+1): #downward
                matrix[i][colEnd] = num
                num += 1
            colEnd -= 1
            for i in xrange(colEnd, colStart-1, -1): #leftward
                matrix[rowEnd][i] = num
                num += 1
            rowEnd -= 1
            for i in xrange(rowEnd, rowStart-1, -1): #upward
                matrix[i][colStart] = num
                num += 1
            colStart += 1
        return matrix
s = Solution()
print s.generateMatrix(5)