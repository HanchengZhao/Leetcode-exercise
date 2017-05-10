class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            row_len = len(matrix)
            col_len = len(matrix[0])
            shift = [[0] * row_len for i in xrange(col_len)]
            x, y = 0, row_len-1
            for row in xrange(len(matrix)):
                for col in xrange(len(matrix[0])):
                    shift[x][y] = matrix[row][col]
                    if x == col_len-1:
                        y -= 1
                        x = 0
                    else:
                        x += 1
        for i in xrange(row_len):
            for j in xrange(col_len):
                matrix[i][j] = shift[i][j]
        return matrix
s = Solution()
print (s.rotate([[1,2],[3,4]]))