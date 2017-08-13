# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
'''
2 pass solution, find the candidate in the first pass and validate it 
in the second
'''
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in xrange(n):
            if knows(candidate, i):
                candidate = i
        for i in xrange(n):
            if i != candidate and knows(candidate, i) or not knows(i, candidate):
                return -1
        return candidate