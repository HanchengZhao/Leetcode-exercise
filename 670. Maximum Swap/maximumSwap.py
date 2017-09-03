class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = list(str(num))
        for i in xrange(len(a)):
            curmax = -1 # because all digits are non-negative
            for ind, val in enumerate(a[i:]): # get the maxval of substring after i
                if curmax <= val:
                    indmax, curmax = ind, val 
            if a[i] != curmax: # if max is not the first, swap
                a[i], a[i+indmax] = curmax, a[i]
                break
        return int(''.join(a))