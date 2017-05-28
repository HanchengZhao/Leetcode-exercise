class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        Min, Max = 0, len(matrix) * len(matrix[0])-1
        col = len(matrix[0])
        while Min <= Max:
            index = (Min + Max) / 2
            midvalue = matrix[index / col][index % col]
            if midvalue == target:
                return True
            elif midvalue > target:
                Max = index-1
            else:
                Min = index+1
        return False