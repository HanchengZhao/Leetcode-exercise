class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [] * (n + 1)
        # initial state of dp
        G[0] = 1
        G[1] = 1

        # G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0)
        for i in xrange(2, n):
            j = 1
            while j <= i:
                G[i] = G[j-1] * G[i-j]

        return G[n]

s = Solution()
print s.numTrees(5)