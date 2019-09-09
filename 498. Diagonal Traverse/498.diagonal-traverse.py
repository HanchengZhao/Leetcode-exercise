#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#


class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        # down to up direction
        reverse = True
        for i in range(0, m+n+1):
            if reverse:
                # since maximum row index is m-1
                # so start col can't be smaller than i-(m-1)
                start_col = max(0, i-(m-1))
                # col can't be bigger than n-1
                for j in range(start_col, min(n, i+1)):
                    res.append(matrix[i-j][j])
            else:
                start_row = max(0, i-(n-1))
                for j in range(start_row, min(m, i+1)):
                    res.append(matrix[j][i-j])
            reverse = not reverse
        return res
