class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        while matrix:
            ret += matrix.pop(0) # rightward
            if matrix and matrix[0]: # downward
                for row in matrix:
                    ret.append(row.pop())
            if matrix: #leftward
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]: #upward
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret
s = Solution()
print s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
