class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        row, col = m-1, 0
        while row >= 0 and col < n:
            val = matrix[row][col]
            if val < target:
                col += 1
            elif val > target:
                row -= 1
            else:
                return True
        return False


'''
start from the end row and column 0, then get close to the target 
by changing the row and column number

time: O (m + n)
'''
