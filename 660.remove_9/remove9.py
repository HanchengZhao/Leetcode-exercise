'''
Here is the observation:
up to int    num that contains 9    index
10           1                       9
100          1*9+10  = 19            81
1000         19*9+100 = 271          729
...

so we can see that the index column is increased by multiplying 9.
Then we save this mapping and divide n by the largest index we can find, record it 
and do it iteratively
'''
class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        nines = [1]
        for i in xrange(11):
            last = nines[-1]
            nines.append(last*9) # save mapping
        res = 0
        while n > 0:
            for i in xrange(11):
                if n < nines[i]:
                    break
            res += 10 ** (i-1)
            n -= nines[i-1]
        return res
s = Solution()
print s.newInteger(800000000)