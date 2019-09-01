# use this method to find all the prime numbers: https://www.geeksforgeeks.org/sieve-of-eratosthenes/

import math


class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [True for i in range(n+1)]
        modulo = 10 ** 9 + 7
        count = 0
        p = 2
        while p * p <= n:
            # start from p^2, because all the not prime numbers
            # have been traversedµ
            if primes[p]:
                for j in range(p * p, n+1, p):
                    primes[j] = False
            p += 1
        count = sum(primes[2:])
        return (math.factorial((n-count)) * math.factorial(count)) % modulo
