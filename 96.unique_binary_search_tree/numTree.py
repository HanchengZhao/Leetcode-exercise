class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0] * (n + 1)
        
        G[0] = 1  # initial state of dp
        G[1] = 1

        # G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0)
        for i in xrange(2, n+1):
            for j in xrange(i+1):
                G[i] += G[j-1] * G[i-j]
                
        return G[n]