class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        for i in xrange(n / 2, 0, -1):
            if n % i == 0:
                divisor = i
                break
        if divisor == 1:
            return n
        return self.minSteps(divisor) + self.minSteps(n / divisor)
'''
an observation from memoization solution: do not need to check odd or even, they
are the same in calculating
'''