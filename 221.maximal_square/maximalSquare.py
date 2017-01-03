class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        s = [[0] * (m+1) for i in range(2)]
        # print s
        ans = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i-1][j-1] == "0":
                    s[i%2][j] = 0
                else:
                    s[i % 2][j] = min(s[(i-1) % 2][j-1], s[i % 2][j-1], s[(i-1) % 2][j]) + 1
                if s[i%2][j] > ans:
                    ans = s[i%2][j]
        return ans * ans
s=Solution()
print s.maximalSquare(["10100","10111","11111","10010"])