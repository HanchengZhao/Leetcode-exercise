# naive solution:

import math


class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                  41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        modulo = 10 ** 9 + 7
        count = 0
        for p in primes:
            if p <= n:
                count += 1
        return (math.factorial((n-count)) * math.factorial(count)) % modulo
