class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        hashtable = {1:0}
        for i in xrange(2, n+1):
            if i % 2 == 0:
                hashtable[i] = hashtable[i / 2] + 2
            else:
                j = i / 2 # start from the middle point
                while j >= 1:
                    if i % j == 0:
                        hashtable[i] = hashtable[j] + i / j
                        break
                    else:
                        j -= 1
        return hashtable[n]
'''
the idea is to use a hashtable to store the previous result as memoization,
if i is an even number: find its half, copy all and poste, so 2 more operations
if it's an odd number: start from the half, find the biggest divisor and add the
number of quotient. e.g. n = 9, find hashtable[3] and plus 3
time: O(n) (the while loop going back costs much though)
space: O(n)

'''