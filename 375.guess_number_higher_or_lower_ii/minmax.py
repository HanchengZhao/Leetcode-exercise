class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        def getMoney(i, j):
            if i >= j:
                return 0
            if dp[i][j]:
                return dp[i][j]
            temp = float("inf")
            for k in range(i, j + 1):
                # pick k and then max amount of its neighbor
                temp = min(temp, k + max(getMoney(i, k-1), getMoney(k+1, j)))
            dp[i][j] = temp
            return temp

        return getMoney(1, n)
